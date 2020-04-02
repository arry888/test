#!/usr/bin/env python

import os
import requests
from bs4 import BeautifulSoup
import dbMysql as db


def get_img_url(s, url):
    result = []
    response = s.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    img_list = soup.find_all(referrerpolicy="no-referrer")
    for item in img_list:
        img_url = item.attrs['data-original']
        result.append(img_url)
    return result


def download_img(s, img_url_list):
    for item in img_url_list:
        try:
            r = s.get(item)
            img_name = os.path.join('/doutu/', item.split('/')[-1:][0])
            with open(img_name, "wb") as f:
                f.write(r.content)
            print("download images " + img_name + " done")
        except Exception as e:
            print('error job ' + item)
#123
if __name__ == '__main__':

    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False

    page = 1

    for i in range(100):
        #     myurl = 'https://www.doutula.com/article/list/?page={}'.format(page)
        #     img_list = get_img_url(s,myurl)
        #     download_img(s,img_list)
        #     page = page + 1
        url = 'https://www.doutula.com/article/list/?page=2'

        image_lsit = get_img_url(s, url)
        print(image_lsit)




