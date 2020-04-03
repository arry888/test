import requests
from bs4 import BeautifulSoup
import re
import dbMysql as db
i=0
while i <= 100:
    i = i + 1
    url = 'http://www.hao6v.net/dy/index_%d.html' % i

    res = requests.get(url)
    res.encoding = 'gb2312'
    suop = BeautifulSoup(res.text, 'lxml')
    movice_list = suop.find_all("a", target="_blank")

    for item in movice_list:
        movice = item.attrs['href']

        url = re.compile(r'^http://www.hao6v.net/dy/(\d{4}-\d{1,2}-\d{1,2})/.*.html$')
        if not re.search(url, movice):
            continue
        else:
            movice_name = item.text
            # print(movice, movice_name)
            res2 = requests.get(movice)
            res2.encoding = 'gb2312'
            suop2 = BeautifulSoup(res2.text, 'lxml')
            movice_list2 = suop2.find_all('a')
            for i in movice_list2:
                mv = i.attrs['href']
                magnet = re.compile(r'^magnet:.*.$')
                if not re.search(magnet, mv):
                    continue
                else:
                    i = i.text
                    db.add_image(mv, i)
                    print(i)
