from html.parser import HTMLParser
import urllib.request
import re


class MyHTMLParser(HTMLParser):
    IsBody = False

    def handle_starttag(self, tag, attrs):
        if (tag == 'body'):
            self.IsBody = True

    def handle_endtag(self, tag):
        if (tag == 'body'):
            self.IsBody = False

    def handle_data(self, data):
        if(self.IsBody):
            print(data[20:34])


myparser = MyHTMLParser()
with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
    html = str(response.read())


myparser.feed(html)
