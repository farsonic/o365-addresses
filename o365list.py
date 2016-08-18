#!/usr/bin/python

from jxmlease import Parser
import urllib
from netaddr import *
import os

o365parser = Parser()
o365list = []
count = 1
list = urllib.urlopen('https://support.content.office.net/en-us/static/O365IPAddresses.xml').read()

for (_, _, entry) in o365parser(list, generator=['addresslist/address']):
  try:
    ip = IPNetwork(entry)
    if ip.version is 4: 
      o365list.insert(count,ip)
      count = count + 1 
  except AddrFormatError:
    pass

  
with open('o365list.txt', 'w') as file: 
  for entry in sorted(o365list):
    ip_str = str(entry)
    file.write(ip_str + "\n")
  


