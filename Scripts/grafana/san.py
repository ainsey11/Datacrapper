import subprocess
import requests
import re
import psutil
import datetime

from influxdb import InfluxDBClient

# noinspection PyUnresolvedReferences
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# noinspection PyUnresolvedReferences
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

current_time = datetime.datetime.utcnow().isoformat()

sda = psutil.disk_usage('/mount/sda')

influx_payload = [
    {
        "measurement": "Storage Servers",
        "tags": {
            "server": "Matrix"
        },
        "time": current_time,
        "fields": {
            "Name": '/mount/sda',
            "SDA bytes Used": sda.used,
            "SDA bytes Free": sda.free,
            "SDA bytes Total": sda.total,
            "SDA Utilization": sda.percent,
            "SDA IO_Wait": psutil.cpu_times_percent().iowait
        }
    }
]

sdb =  psutil.disk_usage('/mount/sdb')

influx_payload2 = [
    {
        "measurement": "Storage Servers",
        "tags": {
            "server": "Matrix"
    },
        "time": current_time,
        "fields": {
            "Name": '/mount/sdb',
            "SDB bytes Used": sdb.used,
            "SDB bytes Free": sdb.free,
            "SDB bytes Total": sdb.total,
            "SDB Utilization": sdb.percent,
            "SDB IO_Wait": psutil.cpu_times_percent().iowait
            }
    }
]


cpu = psutil.cpu_percent()

influx_payload3 = [
    {
        "measurement": "Storage Servers",
        "tags": {
            "server": "Matrix"
    },
        "time": current_time,
        "fields": {
            "Name": 'Cpu Usage',
            "CPU Used Percent": cpu,
            }
    }
]

ram =  psutil.virtual_memory()

influx_payload4 = [
    {
        "measurement": "Storage Servers",
        "tags": {
            "server": "Matrix"
    },
        "time": current_time,
        "fields": {
            "Name": 'RAM',
            "RAM Total": ram.total,
            "RAM Available": ram.available,
            "RAM Percent": ram.percent,
            "RAM Used": ram.used,
            "RAM Free": ram.free,
            "RAM Active": ram.active,
            "RAM Inactive": ram.inactive,
            }
    }
]


influx = InfluxDBClient('matrix', 8086, 'root', 'root', 'storage')
influx.write_points(influx_payload)
influx.write_points(influx_payload2)
influx.write_points(influx_payload3)
influx.write_points(influx_payload4)

