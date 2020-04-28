# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:13:36 2020

@author: shubh
"""

from flask import Flask
from flask import jsonify
from flask import request
import client
 
app = Flask(__name__)
@app.route('/com/pdftotextapi/<company>/<source>',methods=['GET'])
def gettext(company, source):
    text_ = client.client_1(company, source)
    return text_#jsonify({'CONTENT':text_})

#if __name__ == '__main__':
# app.run()