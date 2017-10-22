import sys

try:
        (scriptname, notification_type, notification_title, notification_text, parameters) = sys.argv
except:
        print "No commandline parameters found"
        sys.exit(1)

import requests
messageurl = "http://localhost/api/pushnotif.php?name="+str(notification_title)+str(notification_text)
r = requests.get(messageurl)
print r.status_code
