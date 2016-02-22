import urllib2
import json
import os
import getpass

url = 'http://www.reddit.com/r/InternetisBeautiful/top.json' 

def main():
	
	obj = urllib2.urlopen(url)

	
	data = json.load(obj)

	
	count = 0
