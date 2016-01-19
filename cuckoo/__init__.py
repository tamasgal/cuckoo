# coding=utf-8
# Filename: __init__.py
"""
Cuckoo is a logger which only logs once in a given time interval.
This class is useful if you want to filter massive terminal output.

"""
from __future__ import division, absolute_import, print_function

from datetime import datetime


class Cuckoo(object):
    def __init__(self, interval=0, callback=print):
        self.interval = interval
        self.callback = callback
        self.timestamp = None

    def msg(self, message=None):
        if self.timestamp is None or self._interval_reached():
            self.callback(message)
            self.reset()

    def reset(self):
        self.timestamp = datetime.now()

    def _interval_reached(self):
        return (datetime.now() - self.timestamp).total_seconds() > self.interval
