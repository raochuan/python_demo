#-*-coding:utf-8-*-
import sys
import requests
import time
import re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

base_url = 'http://su.58.com'
add_url = '/ershoushebei'
num = 0
page = 1
nowtime = time.time()

while(True):
    try:
        if page > 5:
            break
        first_page = requests.request('get', base_url+ add_url).content
        soup = BeautifulSoup(first_page, "lxml")
        title_list = [i.get_text() for i in soup.select("a.t")]
        for i in title_list:
            num+=1
            print(i.replace('   ','0'))
        try:
            add_url = '/ershoushebei/pn2%d' % page
            page += 1
        except:
            break
        time.sleep(5)
    except Exception as e:
        print(e)
        break

