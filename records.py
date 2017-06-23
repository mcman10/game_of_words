#!/usr/bin/python
# -*- coding: utf-8 -*-
"""game of words hall of fame"""
from operator import itemgetter

FILE="records.txt"

def get_records():
    lst = []
    try:
        f = open(FILE, 'r')
        for line in f:
            #print line.split('\t')
            pass

    except:
        return [[0,u'ба',u'ноунейм', 0]]

def add_record(score, syl, name, time):
    with open(FILE) as fin:
            lines = [line.split() for line in fin]
    lines.append([str(score),syl,name,time])
    print 1,lines
    sorted(lines, key=itemgetter(3), reverse=True)
    for l in lines:
        l[0] = int(l[0]) 
    sorted(lines, key=itemgetter(0))
    #lines.sort(key = itemgetter(0))
    for l in lines:
        l[0] = str(l[0])
    #print lines
    with open(FILE, 'w') as fout:
            for el in list(reversed(lines)):
                        fout.write('{0}\n'.format('\t '.join(el)))


