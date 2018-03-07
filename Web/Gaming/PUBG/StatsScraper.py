from __future__ import print_function
from selenium import webdriver          # python -m pip install selenium
from bs4 import BeautifulSoup           # python -m pip install bs4
from influxdb import InfluxDBClient    #pip install influxdb
from datetime import datetime

"""
Because this web page uses javascript to render most of it's elements, we can't simply request the HTML from it.
Python isn't a web browser, so it doesn't know how to process all the javascript that a browser handles for you,
as a result, it won't be able to create the html elements you'd see on a web page, instead it would simply get
the HTML the web server sends for your browser to process. And have a bunch of {{ tags }} in place for javascript
to render.

This is why I've used a popular packages, selenium, combined with chromes web driver, which we'll use to tell python 
how the HTML would look after the javascript has been executed. This causes a little problem, as

You may get the below error when executing...
'chromedriver' executable needs to be in PATH.

You can fix this by going to https://sites.google.com/a/chromium.org/chromedriver/downloads and downloading the
latest release to your system path. Or do what I did and drag & drop it into your python directory, since it's
already a systorem path.

This file simply acts as a web browser for python, we we will tell selenium to use as it's engine.
"""
current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')


# Settings, change me up yo!
url = 'https://pubgtracker.com/profile/pc/AnalSod0my/solo?region=agg'
grab = ['Kills', 'Losses', 'K/D Ratio']

# First, we create some options for our driver, and use said options to create the driver as headless.
options = webdriver.ChromeOptions()
options.binary_location = 'chromedriver'
options.binary_location = '/opt/google/chrome/google-chrome'
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

# Next, we ask it to go and render all the JS bullshit on the webpage and spit it back out, we also ask it to
# wait a few seconds incase there's any timed javascript.
driver.get(url)
driver.implicitly_wait(0.2)

# And now we can pull through all the rendered html.
html = driver.page_source

# Part 2, we can feed this html into beautifulsoup and pull anything we want from it.
soup = BeautifulSoup(html, 'html.parser')

# All the stats are contained within their own div with the class "match-stat", use inspect element to find this.
# So we willy simply create a list of all these entries to iterate over.
all_data = soup.findAll('div', {'class': 'match-stat'})

# For every entry in this list, find the span with the class "name" and see if it's what we want from our grab setting.
output = {}  # We will update this with our findings :-)
grab = [x.lower() for x in grab]  # Make your settings all lowercase so we can compare the two in lowercase.
for x in all_data:
    cur_name = x.find('span', {'class': 'name'}).text  # Store the value for tidy code...
    if  cur_name.lower() in grab:  # If the current name is contained in our grab list
        cur_val = x.find('span', {'class': 'value'}).text
        output.update({cur_name: cur_val})

                # All done! Have some fun!
print('Available Keys:', output.keys())
print('Example:', output['Losses'])

json_Loss_Count = [
        {
            "measurement": "Loss_Count",
            "tags": {
                "Player": "AnalSod0my"
                },
            "time" : current_time,
            "fields": {
                "value": output['Losses']
                }
            }
        ]
json_Kills = [
        {
            "measurement": "Kills",
            "tags": {
                "Player": "AnalSod0my"
                },
            "time" : current_time,
            "fields": {
                "value": output['Kills']
                }
            }
        ]
json_KD_Ratio = [
        {
            "measurement": "KD_Ratio",
            "tags": {
                "Player": "AnalSod0my"
                },
            "time" : current_time,
            "fields": {
                "value": output['K/D Ratio']
                }
            }
        ]

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'pubg')
client.write_points(json_Loss_Count)
client.write_points(json_Kills)
client.write_points(json_KD_Ratio)

#if float(output['K/D Ratio']) < 1:


print('\n Losses:', output['Losses'])
print('\n Kills:', output['Kills'])
print('\n K/D Ratio:', output['K/D Ratio'])

print('\nI fucking suck at this game.')
