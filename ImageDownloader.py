#! /usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        ImageDownloader
# Purpose:
#
# Author:      Itabashi
#
# Created:     13/10/2015
# Copyright:   (c) Itabashi 2015
# Licence:     <your licence>
#
# Description:Image Download from Flickr
#-------------------------------------------------------------------------------

# Key:
# 8f0f360a7dd2814b38acdd3142e993f4
#
# Secret:
# 1eba44995d5ecb24

import json
import requests
import os
import shutil
import sys
import urllib2
import re
import pickle
import time

def GoBack1Day(times):
    sec_int = int(times[17:19])
    min_int = int(times[14:16])
    hour_int = int(times[11:13])
    day_int = int(times[8:10])
    month_int = int(times[5:7])

    #00秒の場合

    if day_int == 1:
        month_int = month_int - 1
        day_int = 30
        newtime = times[0:5] + str(month_int).rjust(2, "0") + "-" + str(day_int).rjust(2, "0") + " " + str(hour_int).rjust(2, "0") + ":" + str(min_int).rjust(2, "0") + ':' + str(sec_int).rjust(2, "0")
    else:
        day_int = day_int - 1
        newtime = times[0:8] + str(day_int).rjust(2, "0") + " " + str(hour_int).rjust(2, "0") + ":" + str(min_int).rjust(2, "0") + ':' + str(sec_int).rjust(2, "0")

    return newtime

def image_retrieval(search_words, imnum, max_taken_dates):

    #Flickrアクセスのためのキー
    url = 'https://api.flickr.com/services/rest/'
    API_KEY = '8f0f360a7dd2814b38acdd3142e993f4'

    page = 1;              #ページ
    result = []

    min_taken_dates = GoBack1Day(max_taken_dates)
    dataset_dir = "./" + search_words
    if not os.path.exists(dataset_dir):
        os.mkdir(dataset_dir)
    dataset_dir = "./" + search_words + "/data"
    if not os.path.exists(dataset_dir):
        os.mkdir(dataset_dir)
    img_path = open("./" + search_words + "/imgURL.txt", 'w')

    #検索
    imsum = 0
    while imsum < imnum:
    	print imsum
        payload = {
            'method':'flickr.photos.search',
            'api_key':API_KEY,
            'tags': search_words,
            'page':'1',
            'per_page': '500',
            'max_taken_date':max_taken_dates,
            'min_taken_date':min_taken_dates,
            'content_type':'1',
            'format': 'json',
            'nojsoncallback': '1',
            'sort':'date-taken-desc',
            'extras':'description,license,date_upload,date_taken,owner_name,geo,tags,url_l'
            }
        r = requests.get(url, params=payload)

        #デコード
        for x in r.json()["photos"]["photo"]:
            if not x.has_key("url_l") or not x.has_key("tags"):
                continue

            path = dataset_dir + "/" + x["id"] + "_" + x["secret"]

            #画像URL生成
            temp_img_path = x["url_l"]
            temp_img_path = temp_img_path[0:4] + temp_img_path[5:]
            img_path.write(temp_img_path + "\n")

            #タグの保存
            f = open(path+".txt", 'w')
            f.write(x["tags"])
            f.close()

            #その他の情報の保存
            f = open(path+" etc.txt", 'w')
            keys = x.keys()
            for y in keys:
                f.write(y + ":")
                f.write(str(x[y]))
                f.write("\n")
            f.close()
            imsum = imsum + 1
        max_taken_dates = GoBack1Day(max_taken_dates)
        print max_taken_dates
        min_taken_dates = GoBack1Day(min_taken_dates)
        print min_taken_dates

    print search_words + " end"
    img_path.close()

def main():
    print u"Please enter your search word"
    searchWord = raw_input()
    print u"Please enter the number of acquisition"
    imageNum = raw_input()
    print u"Please enter the recent shooting date and time"
    print u"format exsample:2015-11-02"
    print u"※get back from entered date"
    print u"※It required by the specifications of the API"
    max_taken_dates = raw_input()
    max_taken_dates = max_taken_dates + " 00:00:00"
    image_retrieval(searchWord, imageNum, max_taken_dates)

    print u""

if __name__ == '__main__':
    main()


