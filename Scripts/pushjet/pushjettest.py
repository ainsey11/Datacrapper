import pushjet
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read ('config.ini')

ServiceName = config.get("NotifService","ServiceName")
FaviconURL = config.get("NotifService","FaviconURL")

my_service = pushjet.Service.create(ServiceName,FaviconURL)

ShowKeys = config.get("Keys","ShowKeys")

if ShowKeys == True:
        print('Secret Key: %s' % my_service.secret_key)
        print('Public Key: %s' % my_service.public_key)

CreateQR = config.get("QR","CreateQR")

if CreateQR == True:
        import qrcode
        img = qrcode.make(my_service.public_key)
        img.save('')
