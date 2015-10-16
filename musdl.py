#!/usr/bin/env python

import os
import glob
from bs4 import BeautifulSoup

from urllib2 import urlopen
from urllib import quote_plus as qp
from time import sleep

def output_dir(user_id):
    outputpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'downloads', str(user_id))
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    return outputpath

def song_search(search_term):
    if search_term and search_term != '':
        search_term = qp(search_term)
        try:
            response = urlopen('https://www.youtube.com/results?search_query=' + search_term)

            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a'):
                if '/watch?v=' in link.get('href'):
                    video_link = link.get('href')
                    break

            title = soup.find("a", "yt-uix-tile-link").text
        except:
            title = 'Not Found'
            video_link = ''
        return {'title':title, 'video_link':video_link}

def song_download(video_link, user_id, title):
    outputdir = output_dir(user_id)
    video_link = 'http://www.youtube.com{0}'.format(video_link)
    command = '''youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 --output '{0}/%(title)s.%(ext)s' "{1}"'''.format(outputdir, video_link)
    os.system(command)
    sleep(5)
    return outputdir, title + '.mp3'
