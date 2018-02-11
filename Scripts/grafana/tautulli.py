import requests
import geohash

import datetime
from influxdb import InfluxDBClient

# noinspection PyUnresolvedReferences
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# noinspection PyUnresolvedReferences
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

current_time = datetime.datetime.utcnow().isoformat()

payload = {'apikey': 'e03c76669816cec5c77fb5e8ecb78804', 'cmd': 'get_activity'}
activity = requests.get('http://matrix:8181/api/v2', params=payload).json()['response']['data']

sessions = {d['session_id']: d for d in activity['sessions']}

influx_payload = [
    {
        "measurement": "Tautulli",
        "tags": {
            "type": "stream_count"
        },
        "time": current_time,
        "fields": {
            "current_streams": int(activity['stream_count'])
        }
    }
]

for session in sessions.keys():
    lookup = requests.get('http://freegeoip.net/json/{}'.format(sessions[session]['ip_address_public'])).json()
    influx_payload.append(
        {
            "measurement": "Tautulli",
            "tags": {
                "type": "Session",
                "region_code": lookup['region_code'],
                "name": sessions[session]['friendly_name']
            },
            "time": current_time,
            "fields": {
                "name": sessions[session]['friendly_name'],
                "title": sessions[session]['full_title'],
                "quality": '{}p'.format(sessions[session]['video_resolution']),
                "transcode_decision": sessions[session]['transcode_decision'],
                "location": lookup['city'],
            }
        }
    )

influx = InfluxDBClient('matrix', 8086, 'root', 'root', 'plex')
influx.write_points(influx_payload)

