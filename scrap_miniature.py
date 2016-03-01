"""
# -*- coding: utf-8 -*-
# To download miniature calendar images 
# usage: python scrap_miniature.py 
# @Author: aungthurhahein
# @Date:   2016-02-29 11:10:34
# @Last Modified by:   aungthurhahein
# @Last Modified time: 2016-03-01 14:18:49
"""

import os
import time
import calendar
import argparse
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib import urlretrieve

# Base URL of website
baseurl = "http://miniature-calendar.com/"
# time variable
local = time.localtime()

# function that scrap src of images
def get_miniature(url,filename):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    outpath = os.path.join(out_folder, filename)
    # This is the html component we are looking for
    # <p><img alt="" class="alignnone size-full wp-image-8908" height="1080" src="http://miniature-calendar.com/wp-content/uploads/2016/02/160202tue.jpg" title="Sand shot" width="1080"/></p>    
    img = soup.find(attrs={"height" : "1080"})    
    print img["src"]+ " is downloading..."
    urlretrieve(img["src"], outpath)

#download today image
def daily():        
    today = str(time.strftime("%y%m%d",local)) 
    absurl = baseurl+today     # concat baseURL with yymmmdd folderr today
    file_ = today+"_min.jpg"    
    get_miniature(absurl,file_)    

# download photos of the whole month 
def monthly(yy,mm):
    # get folder structure like http://miniature-calendar.com/160126/ (baseurl/yymmdd/)
    # iterate for whole month
    for i in range(0,calendar.monthrange(yy,mm)[1]):
        day = str(yy)+str(format(mm,'02'))+str(format(i+1,'02'))
        absurl = baseurl+day    # concat baseURL with yymmdd and each days in month
        file_ = day+"_min.jpg"        
        get_miniature(absurl,file_)

# create flat file with download folder path
def out_path():
    out_file = open(".outpath",'w')
    print "folder path to download images (default:~/Downloads/miniature-calendar/)"
    file_dir = raw_input("> ")
    if file_dir == "":
        os.mkdir(os.path.expanduser("~/Downloads/miniature-calendar/"))
        out_file.write("~/Downloads/miniature-calendar/")
    else:        
        out_file.write(file_dir)
    out_file.close()

# read output file location
def read_file_path():
    outpathfile = open('.outpath', 'r')
    file_dir = outpathfile.read()
    if (os.path.isdir(file_dir)):    
        return file_dir
    else:
        print "Invalid file path!"
        print "Folder created at this path: "+ file_dir
        os.mkdir(os.path.expanduser(file_dir))
        return file_dir

def ParseCommandLine():
    parser = argparse.ArgumentParser('Download daily miniature photos from miniature-calendar.com')
    parser.add_argument('-d','--daily', help='Download today photo')
    parser.add_argument('-m','--monthly', type=int, help='Download for the whole month (yymm) e.g. "1602" for 2016 February')    
    theArgs = parser.parse_args()
    return theArgs

if __name__ == "__main__":
    if os.path.isfile(".outpath") is False:
        out_path()
    else:
        out_folder = read_file_path()
        print "Images are downloading to " + out_folder
        args = ParseCommandLine()
        print args
        # monthly(16,02)
    
    # main(args.website)
