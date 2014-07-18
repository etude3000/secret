#!/usr/bin/python

class ncaa:
    '''Who's got class'''
    def __init__(self, name):
        self.who = [name]
    y = 1965
    def who_else(self, othername):
        self.who.append(othername)
    def f(self):
        whoall = ','.join(self.who)
        return whoall + ': No class at all'
