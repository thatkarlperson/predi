#!/usr/bin/env python3

from flask import Flask, render_template
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


@app.route('/')
def show():
    return render_template('market.html', market=m)

