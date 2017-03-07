#!/usr/bin/env python

import predi

m = predi.Market('The ponies will pwn!', 0.5)
m.Bid('George', 0.6)
m.Bid('Anna', 0.7)
m.Bid('Dave', 0.5)
m.Bid('Balloon', 0.4)
m.Bid('Anna', 0.6)
m.Bid('Dave', 0.55)
m.Resolve(True)

for player in m.results:
    print player, m.results[player]


