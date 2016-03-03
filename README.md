# Scrap Miniature

This mini-project started from another design project called <a href="http://miniature-calendar.com/">Miniature Calendar</a>. It's a beautiful creative project, which creates real world scenes with small scaled objects.

I was just thinking a way to download these photos into my local image repository and enjoy. So, why not analyze the site structure and try to scrap these images for inspiration. I think the author might not mind for personal use of these images since these images have been sharing across the social media.

# Dependencies

The following Python libraries are required to install at your machine:

* urllib2 & urllib (likely to be in your python env)
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
* [argparse](https://pypi.python.org/pypi/argparse)

# Usage

At the very first run, the script ask the folder location to store the images. Later on, the images will download to this location automatically. If you wanna change the download folder location, just delete ".outpath" file at your home directory and run the script again.

There are 2 options to retireve images which are

### 1. Download today image

The following option download today photo to the default location.

```
python scrap_miniature.py -d 
```

### 2. Download images of the entire past month

The following option download all images of January 2016 to the default location.

```
python scrap_miniature.py -m 0116     
```

# Usage sugesstion
Use [cron](http://www.cyberciti.biz/faq/linux-when-does-cron-daily-weekly-monthly-run/) to run the script and download images daily/monthly.

# Issues

It is tested *a bit* on Debian linux system. You can kill bugs yourself. 

# License
The project is licensed under [dbad](http://www.dbad-license.org/).

