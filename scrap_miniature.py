"""
# -*- coding: utf-8 -*-
# To extract meta data of ST3 packages
# usage: python get_packagedesc.py list-of-packages.txt
# @Author: aungthurhahein
# @Date:   2016-02-29 11:10:34
# @Last Modified by:   aung
# @Last Modified time: 2016-02-29 16:36:20
"""
import sys
import re
import time
import calendar
from bs4 import BeautifulSoup
from urllib2 import urlopen
# Base URL of website
baseurl = "http://miniature-calendar.com/"
local = time.localtime()
time_fmt = str(time.strftime("%y%m",local))
year = int(time.strftime("%Y",local))
month = int(time.strftime("%m",local))

# get folder structure like http://miniature-calendar.com/160126/ (baseurl/yymmdd/)
# iterate for whole math
for i in range(0,calendar.monthrange(year,month)[1]):
    absurl = baseurl+time_fmt+str(format(i+1,'02'))     # concat baseURL with yymonth and each days in month
    html = urlopen(absurl).read()
    soup = BeautifulSoup(html, "lxml")
    #<p><img alt="" class="alignnone size-full wp-image-8908" height="1080" src="http://miniature-calendar.com/wp-content/uploads/2016/02/160202tue.jpg" title="Sand shot" width="1080"/></p>
    desc = soup.findAll("img")
    # link = soup.find(itemprop="img")
    print desc


