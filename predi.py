#!/usr/bin/env python3
#
# Infra for prediction markets

import math
import collections


# Constants
OPEN = "open"
CLOSED = "closed"
RESOLVED = "resolved"


# Exception classes
class Error(Exception):
    '''Something went wrong.'''


class BidError(Error):
    '''A probability was out of range.

    Code should handle bid errors by rejecting the bid.'''


class MarketError(Error):
    '''A market value (e.g. outcome) was out of range.'''


class Market(object):
    '''A Market represents a proposition with two outcomes.

    A Market can be in three states: OPEN, CLOSED, or RESOLVED.
    If it is OPEN, it can accept bids.  If it is CLOSED, it can't.
    Moving it to RESOLVED requires telling it which outcome was true.
    '''
    def __init__(self, name, house):
        self.name = name
        self.state = OPEN
        self.bids = [('House', house)]  # will be (player, bid)
        self.results = collections.defaultdict(float)
        # results will be player->centibits, populated only at resolution

    def Bid(self, player, bid):
        '''Add a bid that the outcome is true.  Bids are floats in (0, 1).'

        A bid indicates a player's belief that the outcome is true, so 1-bid
        is their belief the outcome is false.
        '''
        if player == 'House':
            raise BidError("House can't raise new bids.")
        if bid <= 0 or bid >= 1:
            raise BidError("Bids are between 0 and 1.")
        if self.state is not OPEN:
            raise BidError("Can't bid on a non-open market.")
        self.bids.append((player, bid))

    def Close(self):
        '''Close the market to new bids.'''
        self.state = CLOSED

    def LastBid(self):
        '''Return the most recent bid.

        Returns: (player, bid)
        '''
        return self.bids[-1]

    def BidHistory(self):
        '''Return the bid history, with the most recent bid last.

        Returns: [(player, bid), ...]
        '''
        return self.bids

    def Resolve(self, outcome):
        '''Resolve the market given a true or false outcome.

        This calculates each player's score in centibits of information
        contributed to the market.

        Returns: dict-like object of player->score
        '''
        if self.state is RESOLVED:
            raise MarketError("Can't resolve a market twice.")
        self.state = RESOLVED
        if outcome not in (True, False):
            raise MarketError('Markets must resolve as true or false for now.')
        # If the outcome was false, invert the sense of all bids.
        correctBids = iter(self.bids) if outcome \
            else ((player, 1-bid) for (player, bid) in self.bids)

        # Add up player scores.
        (_, lastBid) = next(correctBids)  # starts with house bid
        for (player, bid) in correctBids:
            # Score for a correct bid is the difference in log probability
            # from the preceding bid, in centibits.
            logProb = math.log(bid, 2)
            logProbLast = math.log(lastBid, 2)
            score = 100 * (logProb - logProbLast)
            self.results[player] += score
            curBid = bid
        return self.results
