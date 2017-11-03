import socket
import time
import urllib2
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('quizz.teaser.insomnihack.ch',1031))
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

data = s.recv(4000)
print data

while True:
	data = s.recv(4000)
	print data
	if data == "\n":
		continue
	elif data == " ":
		continue
	array1 = data.split(' ')
	print array1
	length = len(array1)
	index = 7
	array2 = []
	while index < length-1:
		array2.append(array1[index])
		index += 1

	url = "https://www.google.ca/search?q=birth+year+of"
	for item in array2:
		url = url +"+"+item
	print url
	req = urllib2.Request(url, headers=hdr)
	webUrl = urllib2.urlopen(req)
	data = webUrl.read()
	lol = data.split('<div class="_XWk">')
	result = lol[1].split(" ")
	final = result[2]
	if result[0][0] == "1":
		final = result[0]
	print final
	s.send(final+'\n')