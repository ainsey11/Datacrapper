import pushjet
import subprocess
from ConfigParser import SafeConfigParser
import qrcode

config = SafeConfigParser()
config.read ('CreateServiceConfig.ini')

ServiceName = config.get("Config","ServiceName")
FaviconURL = config.get("Config","FaviconURL")

my_service = pushjet.Service.create(ServiceName,FaviconURL)

print('Secret Key: %s' % my_service.secret_key)
print('Public Key: %s' % my_service.public_key)

CreateQR = bool(config.get("Config","CreateQR"))

if CreateQR == True:
    img = qrcode.make(my_service.public_key)
    QRSaveLocation = config.get("Config","QRSaveLocation")
    img.save(QRSaveLocation)
