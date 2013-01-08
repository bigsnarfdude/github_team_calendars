#! /usr/bin/env python
'''
github_team_calendar.py
Python program to scrape friends github to build team calendar for github
'''

import requests
user = ""
password = ""
target = ""
my_list=[]

# scraping github accounts
data = !cat github

# cleaning data for targets
for item in data:
    my_list.append(item.split('"')[1].split('/')[-1])

# create csv for scraper
",".join([ "https://github.com/users/%s/contributions_calendar_data" %item for item in my_list ])

# make automated requests for everybodys github calendar data
for item in my_list:
	r = requests.get(('https://github.com/users/%s/contributions_calendar_data' %target), auth=(username, password))

# splitting each piece of data into 2 pieces of data 
for item in r.text.split('],['): 
	print item

