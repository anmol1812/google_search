import importlib
#google = importlib.import_module('/usr/local/lib/python2.7/site-packages/google/__init__.py')
from googlesearch import search
from flask import Flask, request, redirect, url_for, flash, jsonify, Response
import json
import os
import flask
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

app = Flask(__name__)

@app.route('/google_search', methods=['POST'])
def gui_ans():
    if request.method == 'POST':
        query = request.args.get('query')
        def google_scrape(url):
            page = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            thepage = urlopen(page).read()
            #thepage = urllib.request.urlopen(url, headers={'User-Agent': 'Mozilla/5.0'}).read()
            soup = BeautifulSoup(thepage, "html.parser")
            #return soup.title.text
            return soup.title.text
        
        i = 1
        #query = 'gamezop'
        for url in search(query, stop=1):
            a = google_scrape(url)
            print(str(i) + ". " + a)
            #print(url)
            print(" ")
            i += 1
            
    return a

if __name__ == '__main__':
    app.run()