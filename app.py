import json 
import requests
from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route('/')
def index():

    r = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
    
    for coin in r.json():
        #metrics to obtain
        name = (coin["name"])
        price = (coin["price_usd"])
        symbol = (coin["symbol"])

    #convert price string to rounded float -> make shorter?
    price = float(price)
    price = round(price, 2)

    #render index page with price
    return render_template("index.html", price=price)