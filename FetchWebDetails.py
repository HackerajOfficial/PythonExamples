import sys
import urllib2
url=raw_input("Enter Website:") #http://google.com 
url.rstrip()
header=urllib2.urlopen(url).info()
print(str(header))