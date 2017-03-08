#!/usr/bin/env python3

import unittest
import predi

class PrediTest(unittest.TestCase):
    def testMarket(self):
        m = predi.Market('The ponies will pwn!', 0.5)
        m.Bid('Amy', 0.4)
        m.Bid('Bob', 0.1)
        m.Bid('Amy', 0.8)
        m.Bid('Cathy', 0.7)
        m.Bid('Bob', 0.8)
        m.Bid('Drew', 0.9)
        m.Resolve(True)

        second = lambda x: x[1]
        rank = list(m.results.items())
        rank.sort(key=second, reverse=True)
        for player, score in rank:
            print("{} : {} centibits".format(player, score))

        # Check against the teacher's password.
        book = {'Amy': 300 - 32,
                'Bob': -200 + 19,
                'Cathy': -19,
                'Drew': 17}
        for player, score in rank:
            diff = book[player] - score
            self.assertLess(diff, 1, "{} diff too big {}".format(player, diff))


if __name__ == '__main__':
    unittest.main()
