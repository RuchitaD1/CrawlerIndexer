import urllib2
from bs4 import BeautifulSoup
import re
import requests
import sys
reload(sys)
rem=[]
sys.setdefaultencoding('utf8')
def scape(urlText):
    outlinks=[]
    url = urllib2.urlopen(urlText).read()
    soup = BeautifulSoup(url,features="html.parser")
    for line in soup.find_all('a'):
        link=str(line.get('href'))
        rem.append(re.compile('^(file|ftp|mailto):'))
        rem.append(re.compile('.*(/[^/]+)/[^/]+\1/[^/]+\1/'))
        rem.append(re.compile('[?*!@=]'))
        rem.append(re.compile("(?i)\.(gif|jpg|png|ico|css|sit|eps|wmf|zip|ppt|mpg|xls|gz|rpm|tgz|mov|exe|jpeg|bmp|js)$"))
        rem.append(re.compile('(?::\d+)?(?:/|$)'))
        rem.append(re.compile('(?:/|$)'))
        for exp in rem:
            if re.match(exp,link):
                pass
            else:
                outlinks.append(link)

    return outlinks