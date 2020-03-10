from html.parser import HTMLParser
import urllib.request
import re


class MyHTMLParser(HTMLParser):
    lsStartTags = list()
    lsEndTags = list()
    lsData = list()

    def handle_starttag(self, tag, attrs):
        self.lsStartTags.append(tag)

    def handle_endtag(self, tag):
        self.lsEndTags.append(tag)

    def handle_data(self, data):
        self.lsData.append(data)


myparser = MyHTMLParser()

with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
    html = str(response.read())

myparser.feed(html)

ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
ip_address = ip.search(myparser.lsData[2]).group()

print(ip_address)
