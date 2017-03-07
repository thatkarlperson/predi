#!/bin/env python3
#
# Infra for prediction markets

OPEN = object()
CLOSED = object()
RESOLVED = object()


class Error(Exception):
    '''Something went wrong.'''

class BidError(Error):
    '''A probability was out of range.
    
    Code should handle bid errors by rejecting the bid.'''


class Market(object):
    '''A Market represents a proposition with two outcomes.
    A Market can be in three states: OPEN, CLOSED, or RESOLVED.
    If it is OPEN, it can accept Bids.  If it is CLOSED, it can't.
    Moving it to RESOLVED requires telling it which outcome was true.
    '''
    def __init__(self, name, prop):
        self.name = name
        self.prop = prop
        self.state = OPEN
        self.bids = []

    def Bid(self, player, bid1)
        '''Add a bid that the outcome is true.  Bids are floats in [0,1].'
        
        A bid indicates a player's belief that the outcome is true, so 1-bid
        is their belief the outcome is false.'''
        if bid <= 0 or bid >= 1:
            raise BidError("Bids are between 0 and 1.")
        if self.state is not OPEN:
            raise BidError("Can't bid on a non-open market.")
        self.bids.append((player, bid))

    def Close(self):
        self.state = CLOSED

    def Resolve(self, outcome):
        pass

