#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
from flask import Flask, render_template, request, make_response, send_from_directory, send_file
app = Flask(__name__)

import logging
import sys
import datetime
import os
import urllib
from markupsafe import Markup

if not os.path.exists(os.path.join(os.getcwd(), 'logs')):
    try:
        os.mkdir(os.path.join(os.getcwd(), 'logs'))
    except:
        raise

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-15s %(levelname)-8s %(message)s',
                    filename=os.path.join(os.getcwd(), 'logs', '%s_%s.log' % (datetime.datetime.now().strftime("%Y-%m-%d"),os.path.splitext(os.path.split(sys.argv[0])[1])[0])),
                    filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)
formatter = logging.Formatter('%(asctime)s %(name)-15s %(levelname)-8s %(message)s')
console.setFormatter(formatter)

import musdl as mus

def get_setting(key):
    settings = json.loads(open('config.json','r').read())
    return settings.get(key,'')

def get_userid():
    settings = json.loads(open('config.json','r').read())
    userid = settings.get('user_seed')
    userid += 1
    settings['user_seed'] = userid
    with open('config.json','w') as config:
        config.write(json.dumps(settings, indent=4))
    return str(userid)

def get_recent_items(userid):
    filelist = os.listdir(mus.output_dir(userid))
    return filelist

@app.template_filter('urlencode')
def urlencode_filter(s):
    if type(s) == 'Markup':
        s = s.unescape()
    try:
        s = s.encode('utf8')
    except:
        s = s.decode('utf8')#print s 
        s = s.encode('utf8')
    s = urllib.quote_plus(s)
    return Markup(s)

@app.route('/ajax/<action>')
def ajax(action):
    if action == 'search':
        res = mus.song_search(request.args.get('search_string'))
        return json.dumps(res)

@app.route('/song_get')
def get_recent():
    userid = request.cookies.get('userid',get_userid())
    filename = request.args.get('filename')
    directory = mus.output_dir(userid)
    return send_file(os.path.join(directory, filename), as_attachment=True)

@app.route('/song_download')
def song_download():
    userid = request.cookies.get('userid',get_userid())
    video_link = request.args.get('video_link')
    title = request.args.get('title')
    directory, filename = mus.song_download(video_link, userid, title)
    return send_file(os.path.join(directory, filename), as_attachment=True)

@app.route('/')
def index():
    userid = request.cookies.get('userid',None)
    if not userid:
        userid = get_userid()
    recent_items = get_recent_items(userid)
    resp = make_response(render_template('index.tpl', recent_items=recent_items))
    resp.set_cookie('userid', userid)
    return resp

if __name__ == '__main__':
    host = get_setting('bindhost')
    port = get_setting('listenport')
    app.run(host=host, port=port)
