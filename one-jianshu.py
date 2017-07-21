#-*-coding:utf-8-*-
import sys
import requests
import time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

base_url = 'http://www.jianshu.com'
add_url = '/recommendations/notes'
num = 0
nowtime = time.time()

while(True):
    try:
        if num > 1000:
            break
        first_page = requests.request('get', base_url+ add_url).content
        soup = BeautifulSoup(first_page, "lxml")
        title_list = [i.get_text() for i in soup.select("a.title")]
        for i in title_list:
            num+=1
            print(i)
        try:
            nowtime = int(nowtime - 1800)
            add_url = '/recommendations/notes?category_id=56&max_id=' + str(nowtime)
        except:
            break
        time.sleep(10)
    except Exception as e:
        print(e)
        break