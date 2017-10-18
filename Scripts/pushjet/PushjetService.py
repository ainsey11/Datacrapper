import pushjet
import subprocess
from ConfigParser import SafeConfigParser
import sys

config = SafeConfigParser()
config.read ('ServiceConfig.ini')

secret_key = config.get("Keys","SecretKey")

service = pushjet.Service(secret_key)

line = str(sys.argv[1])

service.send(line)
