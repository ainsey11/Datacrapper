import requests
import datetime
from influxdb import InfluxDBClient

# noinspection PyUnresolvedReferences
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# noinspection PyUnresolvedReferences
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

current_time = str(datetime.datetime.utcnow().isoformat())

api_key = '3d2a120e3f91426ebc96a536c6315b81'
headers = {'X-Api-Key': api_key}
get_movies = requests.get('http://matrix:7878/api/movie',  headers=headers).json()
movies = {d['tmdbId']: d for d in get_movies}
missing = []
influx_payload = []

for movie in movies.keys():
    if not movies[movie]['downloaded']:
        missing.append((movies[movie]['title'], movies[movie]['tmdbId']))

for movie, id in missing:
    influx_payload.append(
        {
            "measurement": "Radarr",
            "tags": {
                "type": "Missing",
                "tmdbId": id
            },
            "time": current_time,
            "fields": {
                "name": movie
            }
        }
    )

influx = InfluxDBClient('matrix', 8086, 'root', 'root', 'plex')
influx.write_points(influx_payload)

