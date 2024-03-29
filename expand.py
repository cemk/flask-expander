# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import httplib
from urlparse import urlparse
import os

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')

@app.route('/expand')
def expand():    
#    name='wörld'.decode('utf-8')
    url=request.args.get('url', None)
    
    long = urlparse('http://'+url)
    
    conn = httplib.HTTPConnection(long.netloc)
    conn.request("GET", long.path)
    resp=conn.getresponse()
    short=resp.getheader('location')
    
    return render_template('url.html', short=short, url=url)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
