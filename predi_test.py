#!/usr/bin/env python

import predi

m = predi.Market('The ponies will pwn!', 0.5)
m.Bid('Amy', 0.4)
m.Bid('Bob', 0.1)
m.Bid('Amy', 0.8)
m.Bid('Cathy', 0.7)
m.Bid('Bob', 0.8)
m.Bid('Drew', 0.9)
m.Resolve(True)

for player in m.results:
    print "{} {:.1f}".format(player, m.results[player])


