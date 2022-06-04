from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', header='', sub_header='')