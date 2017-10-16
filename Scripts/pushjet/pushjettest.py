import pushjet
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read ('config.ini')

InitialRun = bool(config.get("InitialRun","InitialRun"))

if InitialRun == True:
    ServiceName = config.get("NotifService","ServiceName")
    FaviconURL = config.get("NotifService","FaviconURL")
    my_service = pushjet.Service.create(ServiceName,FaviconURL)

    ShowKeys = bool(config.get("InitialRun","ShowKeys"))

    if ShowKeys == True:
        print('Secret Key: %s' % my_service.secret_key)
        print('Public Key: %s' % my_service.public_key)

    CreateQR = bool(config.get("InitialRun","CreateQR"))

    if CreateQR == True:
        import qrcode
        img = qrcode.make(my_service.public_key)
        QRSaveLocation = config.get("InitialRun","QRSaveLocation")
        img.save(QRSaveLocation)