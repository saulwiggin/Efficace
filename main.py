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
import plotly
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/')
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

@app.route('/analyse')
def sentiment_analysis():
    url = request.args.get('url')

    request_url = 'http://api.factmata.com/api/v0.1/score/url'
    post_data = json.dumps({'url':url})

    r = requests.post(request_url, post_data)

    #wait seconds befre performing a get request
    time.sleep(20)

    get_url = 'https://api.factmata.com/api/v0.1/score/url' + str(url)
    g = requests.get(get_url)

    #return r.text

    # use ploty to make a nice bar chart

    demo_data = [
                0.31600001454353305,
                0.21600000560283603,
                0.375999987125396,
                0.7129999995231621,
                0.597999989986419,
                0.008000000379979,
                0.014000000432133002,
                0.001000000047497
                ]

    entries = ['Hate speech','Hyperpartisan','Cickbait','Sexism','Identity Hate','Insult','Threats']

    graph_data = [go.Bar(entries, demo_data)]
    plotly.iplot(graph_data, filename='sentiment-analysis')
