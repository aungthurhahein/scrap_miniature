"""
# -*- coding: utf-8 -*-
# To download miniature calendar images 
# usage: python scrap_miniature.py 
# @Author: aungthurhahein
# @Date:   2016-02-29 11:10:34
# @Last Modified by:   aungthurhahein
# @Last Modified time: 2016-03-02 12:44:53
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

#create folder and write file path to flat file
def mkdir_(path):
    out_file = open(".outpath",'w')
    if (os.path.isdir(os.path.expanduser(path))):
        print "Folder already exists"
        out_file.write(os.path.expanduser(path))
    else:   
        os.mkdir(os.path.expanduser(path))
        out_file.write(os.path.expanduser(path))
    out_file.close()

# ask user the file path
def out_path():    
    print "folder path to download images (default:~/Downloads/miniature-calendar/)"
    file_dir = raw_input("> ")    
    if file_dir == "":
        mkdir_("~/Downloads/miniature-calendar/")        
    else:
        mkdir_(file_dir)                

# read and validate output file location
def read_file_path():
    outpathfile = open('.outpath', 'r')
    file_dir = outpathfile.read()
    if (os.path.isdir(os.path.expanduser(file_dir))):    
        return file_dir
    else:
        print "Invalid file path!"
        print "Folder created at this path: "+ os.path.expanduser(file_dir)
        os.mkdir(os.path.expanduser(file_dir))
        return file_dir

def ParseCommandLine():
    parser = argparse.ArgumentParser('Download miniature-calendar images.["-d" for today photo.."-m mmyy" to archive photos of entire month.]')
    parser.add_argument('-d','--daily',action="store_true", help='Download today image')
    parser.add_argument('-m','--monthly', help='Download for the whole month (mmyy) e.g. "0216" for February 2016')    
    theArgs = parser.parse_args()
    return theArgs

if __name__ == "__main__":
    # check output filepath
    if os.path.isfile(".outpath") is False:
        out_path()
    else:
        args = ParseCommandLine()
        out_folder = read_file_path()
        if args.daily:            
            print "Today image is downloading to " + out_folder
            daily()
            print ".........Done........."
        elif args.monthly:            
            if len(args.monthly) <4:
                print "pls make sure you input is in this format:mmyy"
            else:
                mm = int(args.monthly[0]+args.monthly[1])
                yy = int(args.monthly[2]+args.monthly[3])
                print "Images are downloading to " + out_folder
                monthly(yy,mm)
                print ".........Done........."
        else:
            print "try again with -h."