# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, render_template, request
import json
import requests
import time

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    return render_template(
    'submitted_form.html',
    name=name,
    email=email,
    site=site,
    comments=comments)

@app.route('/analyse', methods=['POST'])
def sentiment_analysis():
    url = request.args.get('url')

    request_url = 'http://api.factmata.com/api/v0.1/score/url'
    data = {}
    data['url'] = url
    post_data = json.dumps(data)

    r = requests.post(request_url, post_data)

    // wait seconds befre performing a get request
    time.sleep(20)

    g = requests.get('https://api.factmata.com/api/v0.1/score/url' + url)

    print g
