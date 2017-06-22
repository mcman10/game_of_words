#!/usr/bin/python
# -*- coding: utf-8 -*-
"""game of words hall of fame"""

FILE="records.txt"

def get_records():
    lst = []
    try:
        f = open('FILE', 'r')
        for line in f:
            print line.split('\t')

    except:
        return [[0,u'ба',u'ноунейм', 0]]

def add_record(score, syl, name, time):
    f = open('FILE', 'w')


