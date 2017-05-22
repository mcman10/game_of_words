# -*- coding: utf-8 -*-
"""game of words MainWindow"""
from Tkinter import *

BG_COLOR="#0b0bb0"	#"#0000ff"

class MainWindow (Tk):
	def __init__(self,d):
		Tk.__init__(self)
		#self
		self.initialize(d)

	def initialize(self,d):
		""" initialze mainwindow gui"""
		self.configure(background=BG_COLOR)
		w, h = self.winfo_screenwidth(), self.winfo_screenheight()
		self.geometry("%dx%d+%d+%d" % (w/3, h/2,w/3,h/4))
		self.d=d

		"""http://stackoverflow.com/questions/18091133/creating-an-entry-table-on-tkinter"""
		self.entries = {}
		j=1
		for column in range(3,8):
			for row in range(1,column):
				self.entries[10*column+row]=Entry(self,width=column)
				self.entries[10*column+row].pack()#grid(row=j,column=5)
				j+=1
		start_button = Button(self,text='Start',bg=BG_COLOR,fg='yellow',command=self.start_button_click)
		start_button.pack()


	def start_button_click(self):
		for column in range(3,8):
			for row in range(1,column):
				self.entries[10*column+row].delete(0,10)
				self.entries[10*column+row].insert(0,(self.d[10*column+row]))

		"""
		topframe = Frame(self,bg=BG_COLOR)
		topframe.pack(fill=X)
		self.configbutton = Button(topframe,text=u'Config',bg=BG_COLOR,fg='yellow',command=self.configButtonClick)
		self.configbutton.pack(side=RIGHT,fill=NONE,expand=0)
		middleframe = Frame(self,bg=BG_COLOR)
		middleframe.pack(fill=Y,expand=1)
		self.img = ImageTk.PhotoImage(ImageTk.Image.open("logo.png"))
		self.panel = Label(middleframe, image = self.img)
		self.panel.pack(side = "top", fill = NONE , expand = "yes")
		loginframe = Frame(middleframe)
		self.userlabel =Label(loginframe,text=u'Username',bg=BG_COLOR, fg='yellow')
		self.userlabel.grid(column=1,row=1,sticky=NW+SE)
		self.userVariable=StringVar()
		self.userVariable.set("userarm")
		self.userentry =Entry(loginframe,textvariable=self.userVariable)
		self.userentry.grid(column=2,row=1)
		self.passlabel =Label(loginframe,text=u'Password',bg=BG_COLOR, fg='yellow')
		self.passlabel.grid(column=1,row=2,sticky=NW+SE)
		self.passVariable=StringVar()
		self.passVariable.set("11111111")
		self.passentry =Entry(loginframe,textvariable=self.passVariable,show='*')
		self.passentry.grid(column=2,row=2)#,sticky='E')
		self.loginbutton = Button(loginframe,text=u'Login',bg=BG_COLOR,fg='yellow',command=self.loginButtonClick)
		self.loginbutton.grid(column=1,row=3,columnspan=2,sticky=NW+SE)
		loginframe.pack(fill=NONE,expand=1)
		bottomframe = Frame(self,bg=BG_COLOR)
		bottomframe.pack(side="bottom",fill=X)
		self.quitbutton = Button(bottomframe,text=u'Quit',bg=BG_COLOR,fg='yellow',command=self.quitButtonClick)
		self.quitbutton.pack(side="left",fill=NONE,expand=0)

		self.sett.load_from_ini()
		"""
