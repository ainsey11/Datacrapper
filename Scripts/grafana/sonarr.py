import requests
import datetime
from influxdb import InfluxDBClient

# noinspection PyUnresolvedReferences
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# noinspection PyUnresolvedReferences
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

current_time = datetime.datetime.utcnow().isoformat()

api_key = 'f5376518dc9248e7bc0a0be732b47f6f'
headers = {'X-Api-Key': api_key}
get_tv_shows = requests.get('http://matrix:8989/api/wanted/missing/?pageSize=1000',
                            headers=headers).json()['records']
tv_shows = {d['id']: d for d in get_tv_shows}
missing = []
influx_payload = []

for show in tv_shows.keys():
    name = '{} - S{}E{}'.format(tv_shows[show]['series']['title'], tv_shows[show]['seasonNumber'],
                                tv_shows[show]['episodeNumber'])
    missing.append((name, tv_shows[show]['id']))

for show, id in missing:
    influx_payload.append(
        {
            "measurement": "Sonarr",
            "tags": {
                "type": "Missing",
                "sonarrId": id
            },
            "time": current_time,
            "fields": {
                "name": show
            }
        }
    )

influx = InfluxDBClient('matrix', 8086, 'root', 'root', 'plex')
influx.write_points(influx_payload)

