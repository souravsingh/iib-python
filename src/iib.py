import urllib2
import json
import os
import getpass
import webbrowser

url = 'http://www.reddit.com/r/InternetisBeautiful/top.json' 

def main():
	
	obj = urllib2.urlopen(url)

	
	data = json.load(obj)

	for i in data["data"]["children"]:

	  interneturl = i["data"]["url"]
	  try:
  
	    print interneturl
	    
	    os.system("start \"\" "+interneturl)
	   
if __name__ == "__main__":
	main()
