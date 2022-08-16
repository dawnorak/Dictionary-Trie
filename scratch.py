# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:10:00 2022

@author: DAWN
"""

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('templates\ds.html')

@app.route('/submit', methods=['POST'])
def dic():
    search_keyword = request.form['keyword']
    msg=main(search_keyword)
    return render_template('templates\ds.html', msg=msg)

app.run(host='localhost', port=5000)