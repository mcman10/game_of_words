# -*- coding: utf-8 -*-
"""game of words MainWindow"""
import pygtk
pygtk.require("2.0")
import gtk
import datetime
import gobject
from random import randint
from network import check_word
from records import get_records, add_record

#BG_COLOR="#0b0bb0"	

def print_table(d):
	for i in range(3,7):
		for j in range(1,i):
			print d[i*10+j]

def gen_table(syll):
	"""generate a game table as dict d {31:"??`",32:"`??",41:"??``",42:"`??`",...} """
	d = {31:"```",32:"```",41:"````",42:"````",43:"````",51:"`````",52:"`````",53:"`````",54:"`````",
			61:"``````",62:"``````",63:"``````",64:"``````",65:"``````",
			71:"```````",72:"```````",73:"```````",74:"```````",75:"```````",76:"```````"}
	for i in range(3,8):
		for j in range(1,i):
			w=list(d[10*i+j])
			w[j-1]=syll[0]
			w[j]=syll[1]
			d[10*i+j]="".join(w)
	return d

def rand_syll():
	""" generate a random russian syllable """
	vovels={1:'а',2:'е',3:'ё',4:'и',5:'о',6:'у',7:'ы',8:'э',9:'ю',10:'я'}
	conconants={1:'б',2:'в',3:'г',4:'д',5:'ж',6:'з',7:'к',8:'л',9:'м',10:'н',
			11:'п',12:'р',13:'с',14:'т',15:'ф',16:'х',17:'ч',18:'ш',19:'щ'}
	i=randint(1,10)
	j=randint(1,19)
	syllable=(conconants[j],vovels[i])
	return syllable 

class MainWindow (gtk.Window):
	def __init__(self):
            super(self.__class__, self).__init__()
            self.set_title("Game of Words")
            self.connect("delete-event", gtk.main_quit)

            self.score = 0
            self.entries = [[None for col in range(8)] for col in range(20)] 
            self.icons = []
            self.set_position(gtk.WIN_POS_CENTER)
            self.apply_icon = gtk.Image()
            self.cancel_icon = gtk.Image()
            self.question_icon = gtk.Image()
            self.apply_icon.set_from_stock(gtk.STOCK_SPELL_CHECK, gtk.ICON_SIZE_BUTTON)
            self.cancel_icon.set_from_stock(gtk.STOCK_CANCEL, gtk.ICON_SIZE_BUTTON)
            self.question_icon.set_from_stock(gtk.STOCK_DIALOG_QUESTION, gtk.ICON_SIZE_BUTTON)
	    self.initialize()
            self.show_all()

	def initialize(self):
	    """ initialze mainwindow gui"""
            #color = gtk.gdk.color_parse(BG_COLOR)
            #self.modify_bg(gtk.STATE_NORMAL, color)

            # RESIZE MAINWINDOW
            w,h = gtk.gdk.screen_width(), gtk.gdk.screen_height() 
            self.resize(w/2,h/2)

            #TABLE OF ENTRIES WIRH LETTERS
            self.table = gtk.Table(rows=20, columns=8, homogeneous=True)
            letters_alignment = gtk.Alignment(xalign=0, yalign=0.5)
            letters_alignment.add(self.table)

            current_length = 3
            change_length_where_row = 3
            for row in range (20):
                for column in range (7):
                    if column+1 <= current_length: 
                        self.entries[row][column] = gtk.Entry(max=1)
                        self.entries[row][column].set_width_chars(2)
                        self.entries[row][column].get_settings().set_string_property('gtk-font-name', 'sans normal 12','');
                        self.table.attach(self.entries[row][column], column, column+1, row, row+1,
                                xoptions = gtk.SHRINK, yoptions = gtk.SHRINK, xpadding=3,ypadding=3 )
                        self.entries[row][column].show()
                    if row+1 == change_length_where_row: 
                        change_length_where_row += current_length
                        current_length +=1

            settings = gtk.settings_get_default()
            settings.props.gtk_button_images = True


            #INFORMATION LABELS
            self.score_label = gtk.Label(str(self.score))
            self.time_label = gtk.Label("00:00:00")
            time_frame = gtk.Frame(label="time")
            time_frame.add(self.time_label)
            score_frame = gtk.Frame(label="score")
            score_frame.add(self.score_label)
            labels_vbox = gtk.VBox(homogeneous=False, spacing=5)
            labels_vbox.add(time_frame)
            labels_vbox.add(score_frame)
            labels_alignment = gtk.Alignment(xalign=0.5, yalign=0.05, xscale = 0.95)
            labels_alignment.add(labels_vbox)

            #CONTROL BUTTONS
            self.start_button = gtk.Button(label="start")
            self.check_button = gtk.Button(label="check")
            self.fame_button = gtk.Button(label="hall of fame")
            self.check_button.connect("clicked", self.check_button_clicked)
            self.check_button.set_sensitive(False)
            self.start_button.connect("clicked", self.start_button_clicked)
            button_vbox = gtk.VBox(homogeneous=True, spacing=5)
            button_vbox.add(self.start_button)
            button_vbox.add(self.check_button)
            button_vbox.add(self.fame_button)

            buttons_alignment = gtk.Alignment(xalign =0.9, yalign=0.05, xscale=0.95)
            buttons_alignment.add(button_vbox)

            main_hbox = gtk.HBox(homogeneous=False, spacing=0);

            main_hbox.add(letters_alignment)
            main_hbox.add(labels_alignment)
            main_hbox.add(buttons_alignment)
            self.add(main_hbox)

        def set_letters(self, d):
            row, column = 0,0 
            for i in range (3,8):
                for j in range (1,i):
                    for c in d[i*10+j].decode('utf-8'):
                        self.entries[row][column].set_text(c)
                        column +=1
                    column = 0
                    row+=1

	def start_button_clicked(self, widget, data=None):
            self.score = 0 
            self.score_label.set_text(str(self.score))
            self.running = True
            syll = rand_syll()
            d=gen_table(syll)
            self.set_letters(d)
            self.set_table_icons_question()
            self.start_time = datetime.datetime.now()
            gobject.timeout_add(100, self.tired_task)
            self.start_button.set_sensitive(False)
            self.check_button.set_sensitive(True)

        def tired_task(self):
            self.time_label.set_text(str(datetime.datetime.now()-self.start_time))
            return self.running

	def check_button_clicked(self, widget, data=None):
            records_list = get_records()
            #print records_list
            self.running = False
            self.time_label.set_text(str(datetime.datetime.now()-self.start_time))
            self.start_button.set_sensitive(True)
            self.check_button.set_sensitive(False)
            lst =  self.collect_words()
            i = 0
            for word in lst:
                #print check_word(word)
                if check_word(word):
                    self.score += len(word) 
                    self.score_label.set_text(str(self.score))
                    self.icons[i].clear()
                    self.icons[i].set_from_stock(gtk.STOCK_SPELL_CHECK, gtk.ICON_SIZE_BUTTON)
                    self.icons[i].queue_draw()
                    while (gtk.events_pending ()):
                            gtk.main_iteration ();
                    #print 'True'
                else:
                    self.icons[i].clear()
                    self.icons[i].set_from_stock(gtk.STOCK_CANCEL, gtk.ICON_SIZE_BUTTON)
                    self.icons[i].queue_draw()
                    while (gtk.events_pending ()):
                            gtk.main_iteration ();
                    #print 'False'
                i+=1

        def collect_words(self):
            list = []
            for row in range (20):
                word = ""
                for column in range (7):
                    if self.entries[row][column]:
                        letter = self.entries[row][column].get_text() 
                        word += letter.decode('utf-8')
                #print word
                            
                list.append(word)
            return list

        def set_table_icons_question(self):
            for icon in self.icons :
                icon.clear()
                #icon.queue_draw()
                del(icon)
            self.icons = []
            for i in range (20):
                icon = gtk.Image()
                icon.set_from_stock(gtk.STOCK_DIALOG_QUESTION, gtk.ICON_SIZE_BUTTON)
                self.table.attach(icon, 7,8,i,i+1, xoptions = gtk.SHRINK, yoptions = gtk.SHRINK, xpadding= 1, ypadding=1)
                self.icons.append(icon)
                icon.show()
