from html.parser import HTMLParser
import urllib.request
import pprint


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.IsTbody = False
        self.IsA = False
        self.IsKey = False
        self.IsValue = False
        self.IsTd = False
        self.key = ''
        self.color = dict()

    def handle_starttag(self, tag, attrs):
        if (tag == 'tbody'):
            self.IsTbody = True
        if (tag == 'td'):
            self.IsTd = True
        if(tag == 'a' and attrs[0][0] == 'class'):
            self.IsA = True
            self.IsKey = True
        if (tag == 'a' and attrs[0][0] == 'href'):
            self.IsA = True
            self.IsValue = True

    def handle_endtag(self, tag):
        if (tag == 'a'):
            self.IsA = False
            self.IsKey = False
            self.IsValue = False
        if (tag == 'td'):
            self.IsTd = False
        if (tag == 'tbody'):
            self.IsTbody = False

    def handle_data(self, data):
        if(self.IsTbody and self.IsTd and self.IsA and self.IsKey):
            self.key = ''
            self.key = data

        if(self.IsTbody and self.IsTd and self.IsA and self.IsValue
           ):
            self.color.update({self.key: data})
        return self.color


myparser = MyHTMLParser()
with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
    html = str(response.read())

myparser.feed(html)

pprint.pprint(myparser.color)

print ("There are total {:0} colors.".format(len(myparser.color)))
