import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Parsing TradeStation order emails and posting to Twitter... <a href="http://tradingtechnicians.com">tradingtechnicians.com</a>'
