import urllib2
from bs4 import BeautifulSoup

url = "https://pubgtracker.com/profile/pc/AnalSod0my/solo?region=agg"
headers = {'User-Agent':'Mozilla/5.0'}
req = urllib2.Request(url, None, headers)
page = urllib2.urlopen(req).read()


soup = BeautifulSoup(page, "lxml")

alldivs = soup.find("script", {"type" : "text/javascript"})
scriptout = alldivs.find_all("var playerData")
print scriptout[0]
