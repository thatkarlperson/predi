#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

from predi import Market

m = Market('The ponies will pwn!', 0.5)
m.Bid('Amy', 0.4)
m.Bid('Bob', 0.1)
m.Bid('Amy', 0.8)
m.Bid('Cathy', 0.7)
m.Bid('Bob', 0.8)
m.Bid('Drew', 0.9)
m.Resolve(True)

n = Market("The cats will cat!", 0.7)
n.Bid('Cathy', 0.5)
n.Bid('Bob', 0.6)
n.Bid('Amy', 0.3)

markets = [m, n]


@app.route('/')
def redirMain():
    return redirect(url_for("listAll"))


@app.route('/markets', methods=['GET'])
def listAll():
    return render_template('allmarkets.html', count=len(markets))


@app.route('/markets', methods=['POST'])
def createMarket():
    return 'nope'


@app.route('/market/<int:market_id>', methods=['GET'])
def showMarket(market_id):
    return render_template('market.html', market=markets[market_id])


@app.route('/market/<int:market_id>', methods=['POST'])
def createBid(market_id):
    return 'nope'

