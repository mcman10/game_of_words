# -*- coding: utf-8 -*-
"""game of words MainWindow"""
import pygtk
pygtk.require("2.0")
import gtk
import operator

#BG_COLOR="#0b0bb0"	

class MainWindow (gtk.Window):
	def __init__(self):
            super(self.__class__, self).__init__()
            self.set_title("Game of Words")
            self.connect("delete-event", gtk.main_quit)

            self.entries = [[None for col in range(7)] for col in range(20)] 
	    self.initialize()
            self.set_position(gtk.WIN_POS_CENTER)
            self.show_all()

	def initialize(self):
	    """ initialze mainwindow gui"""
            #color = gtk.gdk.color_parse(BG_COLOR)
            #self.modify_bg(gtk.STATE_NORMAL, color)

            w,h = gtk.gdk.screen_width(), gtk.gdk.screen_height() 
            self.resize(w/2,h/2)

            letters_alignment = gtk.Alignment(xalign=0, yalign=0.5)
            table = gtk.Table(rows=20, columns=7, homogeneous=True)
            letters_alignment.add(table)

            buttons_alignment = gtk.Alignment(xalign =1, yalign=0)

            main_hbox = gtk.HBox(homogeneous=False, spacing=0);

            main_hbox.add(letters_alignment)
            main_hbox.add(buttons_alignment)
            self.add(main_hbox)

            current_length = 3
            change_length_where_row = 3
            for row in range (20):
                for column in range (7):
                    if column+1 <= current_length: 
                        self.entries[row][column] = gtk.Entry(max=1)
                        self.entries[row][column].set_width_chars(2)
                        self.entries[row][column].get_settings().set_string_property('gtk-font-name', 'sans normal 12','');
                        table.attach(self.entries[row][column], column, column+1, row, row+1, xoptions = gtk.SHRINK, yoptions = gtk.SHRINK, xpadding=3,ypadding=3 )
                        self.entries[row][column].show()
                    if row+1 == change_length_where_row: 
                        change_length_where_row += current_length
                        current_length +=1

        def set_letters(self, d):
            row, column = 0,0 
            for i in range (3,8):
                for j in range (1,i):
                    for c in d[i*10+j].decode('utf-8'):
                        self.entries[row][column].set_text(c)
                        column +=1
                    column = 0
                    row+=1

	def start_button_click(self):
            pass
