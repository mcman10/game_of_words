#!/usr/bin/python
# -*- coding: utf-8 -*-
"""game of words"""
from twisted.internet import gtk2reactor
gtk2reactor.install()
from mainwindow import MainWindow

def main():
	""" main function of game """
	app = MainWindow ()
        from twisted.internet import reactor
        reactor.run()

if __name__ == "__main__":
	main()
