import pushjet
import subprocess
from ConfigParser import SafeConfigParser


config = SafeConfigParser()
config.read ('ServiceConfig.ini')

secret_key = config.get("Keys","SecretKey")

service = pushjet.Service(secret_key)

line = "Test Notification From Matrix"

service.send(line)
