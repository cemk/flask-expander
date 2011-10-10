# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import httplib
from urlparse import urlparse


app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

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

@app.route('/naber')
def naber():
    naber = "naber lov"
    
    return render_template('naber.html', naber=naber)


if __name__ == '__main__':
    app.run()
