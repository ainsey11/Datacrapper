import pushjet
import subprocess
from ConfigParser import SafeConfigParser
import sys

secret_key = str('6e7ae26ce1758cd28edb5251b7cd4142')

service = pushjet.Service(secret_key)

line = str(sys.argv[1])

service.send(line)
