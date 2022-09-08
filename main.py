# do pip install pyshorteners to install
#import pyshorteners 


import pyshorteners

s = pyshorteners.Shortener()

url = str(input('Enter a url you want to short : '))

print(s.tinyurl.short(url))