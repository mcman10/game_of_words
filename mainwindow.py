# -*- coding: utf-8 -*-
"""game of words MainWindow"""
import pygtk
pygtk.require("2.0")
import gtk

BG_COLOR="#0b0bb0"	

class MainWindow (gtk.Window):
	def __init__(self,d):
                super(self.__class__, self).__init__()
                self.set_title("Game of Words")
                self.connect("delete-event", gtk.main_quit)

                self.entries = [[None for col in range(7)] for col in range(20)] 
		self.initialize(d)
                self.set_position(gtk.WIN_POS_CENTER)
                self.show_all()

	def initialize(self,d):
		""" initialze mainwindow gui"""
                color = gtk.gdk.color_parse(BG_COLOR)
                self.modify_bg(gtk.STATE_NORMAL, color)

                w,h = gtk.gdk.screen_width(), gtk.gdk.screen_height() 
                self.resize(w/2,h/2)

                table = gtk.Table(rows=20, columns=7, homogeneous=True)

                current_length = 3
                change_length_where_row = 3
                for column in range (7):
                    for row in range (20):
                        self.entries[row][column] = gtk.Entry()

		j=1
		for column in range(3,8):
			for row in range(1,column):
				#self.entries[10*column+row]=Entry(self,width=column)
				#self.entries[10*column+row].pack()#grid(row=j,column=5)
				j+=1
		#start_button = Button(self,text='Start',bg=BG_COLOR,fg='yellow',command=self.start_button_click)
		#start_button.pack()


	def start_button_click(self):
		for column in range(3,8):
			for row in range(1,column):
				self.entries[10*column+row].delete(0,10)
				self.entries[10*column+row].insert(0,(self.d[10*column+row]))
