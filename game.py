#!/usr/bin/python
# -*- coding: utf-8 -*-
"""game of words"""

from twisted.internet import gtk2reactor
gtk2reactor.install()
from random import randint
from mainwindow import MainWindow

def print_table(d):
	for i in range(3,8):
		for j in range(1,i):
			print d[i*10+j]

def gen_table(syll):
	"""generate a game table as dict d {31:'??.',32:'.??',41:'??..',42:'.??.',...} """
	d = {31:'...',32:'...',41:'....',42:'....',43:'....',51:'.....',52:'.....',53:'.....',54:'.....',
			61:'......',62:'......',63:'......',64:'......',65:'......',
			71:'.......',72:'.......',73:'.......',74:'.......',75:'.......',76:'.......'}
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

def main():
	""" main function of game """
	syll=rand_syll()
	d=gen_table(syll)
	#print_table(d)
	app = MainWindow (d)
	#app.mainloop()
        from twisted.internet import reactor
        reactor.run()

if __name__ == "__main__":
	main()
