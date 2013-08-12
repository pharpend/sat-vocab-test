#!/usr/bin/python

'''
sat_word_chooser.py

Description:
Program that selects five words from the sat_vocab_db database for quizzing. All words will be of the same part of speech. 

Proposed Setup:
Random number generator chooses a number between 1 and 5014. The program picks out that word, as well as four other words of the same part of speech. The program returns a two-dimensional tuple. The first index will be the part of speech of the words in question. The second index will be a tuple of the words. The third index will be a tuple of the definitions.
'''

from random import randint, choice
import sys
import sqlite3 as sql


def main(): # static method for use by other programs
	n = randint(1,5014) # 'random' number between 1 and 5014
	
	dbnom = 'sat_vocab_db.db' # database file name
	get_ln1 = 'SELECT * FROM Vocab WHERE N=%d;' % n # ln1 = line 1
	try:
		conn = sql.connect(dbnom) # open the database
		exc = conn.cursor() # make a cursor
		exc.execute(get_ln1) # get the stuff
	except sql.Error, e:
		print "ERROR: %s" % e.args[0]
		sys.exit(1) #get out
	# end of try/except
	
	ln1 = exc.fetchone() # get usable version
	word_ln1 = ln1[1] # ln1 word
	pos_ln1 = ln1[2] # part of speech of ln1
	def_ln1 = ln1[3] # ln1 definition
	
	get_more_like_ln1 = "select * from Vocab where PartOfSpeech='%s'" % pos_ln1 # command string to get all entries of same part of speech 
	try:
		exc.execute(get_more_like_ln1) # get all with same part of speech as ln1
	except sql.Error, e:
		print "ERROR: %s" % e.args[0]
		sys.exit(1) #get out
	#end of try/except
	
	all_like_ln1 = exc.fetchall() # list of all entries of same pos as ln1
	# print all_like_ln1
	
	ln2 = choice(all_like_ln1) # grabs one of the words similar to ln1
	word_ln2 = ln2[1] # ln2 word
	def_ln2 = ln2[3] # ln2 definition
	
	ln3 = choice(all_like_ln1)
	word_ln3 = ln3[1] # ln3 word
	def_ln3 = ln3[3] # ln3 definition
	
	ln4 = choice(all_like_ln1)
	word_ln4 = ln4[1] # ln4 word
	def_ln4 = ln4[3] # ln4 definition
	
	ln5 = choice(all_like_ln1)
	word_ln5 = ln5[1] # ln5 word
	def_ln5 = ln5[3] # ln5 definition
	
	pos = pos_ln1 # for appearance sake
	words = (word_ln1, word_ln2, word_ln3, word_ln4, word_ln5) # all of the words
	defs = (def_ln1, def_ln2, def_ln3, def_ln4, def_ln5) # all of the definitions
	
	final_tuple = pos, words, defs # all of the data to be returned
	return final_tuple
# end of main()

if __name__ == '__main__':	main()
# end of if
