from __future__ import print_function
from datetime import datetime           # Used for UTC time
from json import dumps                  # Used for pretty printing...
from bs4 import BeautifulSoup           # python -m pip install bs4
from selenium import webdriver          # python -m pip install selenium
from influxdb import InfluxDBClient     # python -m pip install influxdb

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

This file simply acts as a web browser for python, we will tell selenium to use as it's engine.
"""

# Settings, change me up yo!
url = 'https://pubgtracker.com/profile/pc/AnalSod0my/solo?region=agg'
grab = [
    'Wins', 'Kills', 'Losses', 'K/D Ratio', 'Rounds Played',
    'Win %', 'Time Survived', 'Top 10s', 'Rating', 'AVG DMG PER MATCH'
]

current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

# First, we create some options for our driver, and use said options to create the driver as headless
options = webdriver.ChromeOptions()
options.binary_location = 'chromedriver'
options.binary_location = '/opt/google/chrome/google-chrome'
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

# Next, we ask it to go and render all the JS bullshit on the webpage and spit it back out, we also ask it to
# wait a few seconds incase there's any timed javascript
driver.get(url)
driver.implicitly_wait(0.2)

# And now we can pull through all the rendered html
html = driver.page_source

# We can now feed this html into beautifulsoup and pull anything we want from it
soup = BeautifulSoup(html, 'html.parser')

# All the stats are contained within their own div with the class "match-stat", use inspect element to find this
# So we will simply create a list of all these entries to iterate over
profile_name = soup.find('h1', {'class': 'profile-name'}).text  # Find over findAll will look for the first occurance
all_data = soup.findAll('div', {'class': 'match-stat'})

# For every entry in this list, find the span with the class "name" and see if it's what we want from our grab setting
output = {}  # We will populate this with our findings :-)
grab = [x.lower() for x in grab]  # Make your settings all lowercase so we can compare the two in lowercase
for x in all_data:
    cur_name = x.find('span', {'class': 'name'}).text  # Store the value for tidy code
    if cur_name.lower() in grab:  # If the current name is contained in our grab list
        cur_val = x.find('span', {'class': 'value'}).text
        output.update({cur_name: cur_val})

# Close the driver down to save on sys resources
driver.quit()

# Format the data ready for dumping into the database
to_db = {}
for k, v in output.iteritems():  # Key, Value
    try:  # Try converting every keys value to an int, if it fails, make it a string
        v = int(v)
    except ValueError:
        v = str(v)

    # Populate the dump variable in your desired format
    to_db.update(
        {k: {'measurement': k, 'tags': {'Player': profile_name}, 'time': current_time, 'fields': {'value': v}}}
    )

# Create a database session
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'pubg')

# Send it all to the database. We could of done this in the loop above, but I'm keeping the code readable
for k, v in to_db.iteritems():
    client.write([to_db[k]])  # Noticed you used a lists in your changes, so I've surrounded it in [ ] to keep the same
    print(dumps((k, v), indent=4, sort_keys=True))

print('Available Keys:', to_db.keys())
