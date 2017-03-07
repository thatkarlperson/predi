#!/bin/env python3
#
# Infra for prediction markets

import math
import collections


# Constants
OPEN = object()
CLOSED = object()
RESOLVED = object()


# Exception classes
class Error(Exception):
    '''Something went wrong.'''

class BidError(Error):
    '''A probability was out of range.
    
    Code should handle bid errors by rejecting the bid.'''

class MarketError(Error):
    '''A market value (e.g. outcome) was out of range.'''


# A Market.
class Market(object):
    '''A Market represents a proposition with two outcomes.

    A Market can be in three states: OPEN, CLOSED, or RESOLVED.
    If it is OPEN, it can accept Bids.  If it is CLOSED, it can't.
    Moving it to RESOLVED requires telling it which outcome was true.
    '''
    def __init__(self, name, house):
        self.name = name
        self.state = OPEN
        self.bids = [('House', house)]  # will be (player, bid)
        self.results = collections.defaultdict(float)  # will be player->centibits

    def Bid(self, player, bid):
        '''Add a bid that the outcome is true.  Bids are floats in [0,1].'
        
        A bid indicates a player's belief that the outcome is true, so 1-bid
        is their belief the outcome is false.'''
        if player == 'House':
            raise BidError("House can't raise new bids.")
        if bid <= 0 or bid >= 1:
            raise BidError("Bids are between 0 and 1.")
        if self.state is not OPEN:
            raise BidError("Can't bid on a non-open market.")
        self.bids.append((player, bid))

    def Close(self):
        self.state = CLOSED

    def Resolve(self, outcome):
        self.state = RESOLVED
        if outcome not in (True, False):
            raise MarketError('Markets must resolve as true or false for now.')
        # If the outcome was false, invert the sense of all bids.
        correctBids = iter(self.bids) if outcome else ((player, 1-bid) for (player, bid) in self.bids)
        (_, curBid) = next(correctBids)  # starts with house bid
        # Add up player scores.
        for (player, bid) in correctBids:
            logProb = math.log(bid, 2)
            logProbLast = math.log(curBid, 2)
            score = 100 * (logProb - logProbLast)
            self.results[player] += score
            curBid = bid



