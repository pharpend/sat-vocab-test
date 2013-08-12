#!/usr/bin/python

'''
sat-dber.py

Copyright 2012 Peter Harpending.

Description: 
This program is a dber-series program. It puts raw data into an organized sql database. Said raw data is stored in sat-vocab-text.txt

Raw Data Structure:
Word t. Defintion
abase v. To lower in position, estimation, or the like; degrade.

Proposed Database Structure (5014 rows):
Alphabetical Rank	Word	Part	Definition
1					abase	v.		To lower in position, estimation, or the like; degrade.

Proposed Program Function:
1. Make a database called 'sat_vocab_db.db'
2. Delete table called 'Vocab' (if exists), then make new one
3. Loop over file with readlines() function.
4. Use split() to separate words from definitions.
5. Insert values into table.
'''

# import neccesary packages
import sqlite3 as sql
from time import time
import sys

t0 = time()

def main():	# this is the nerve center of the program
	# this code is a list of predefined strings for later usage
	create_table_command = "CREATE TABLE Vocab(N INT, Word TEXT, PartOfSpeech TEXT, Definition TEXT);" # this command creates the table once we dropped it
	drop_table_command = "DROP TABLE IF EXISTS Vocab;" # this command deletes the table so we don't get duplicate tables		f = open(fnom, 'r') # open fnom in read mode
	dbnom = 'sat_vocab_db.db' # database file name
	
	# attempt to make the database
	try: # sql code throws a good deal of exceptions
		conn = sql.connect(dbnom) #connect to the database
		exc = conn.cursor() # make a cursor
		exc.execute(drop_table_command) # delete any possible duplicate
		exc.execute(create_table_command) # create the table 
	except sql.Error, e: # in the event of an error
		print '%.2f: ERROR: %s' % (time()-t0, e.args[0]) # print the error message
		sys.exit(1) # in event of an error, get out
	#end of try/except
	print 'Database created'
	
	# loop through the file and add the data
	f = open('sat_vocab_text.txt', 'r') # open the file in read-only mode
	n = 1 # integer loop counter
	for fln in f.readlines(): # each individual line is a loop counter
		flnls = fln.split() # transform fln into an array
		word = flnls[0] # get the word
		part = flnls[1] # get the part of speech
		definition_ls = flnls[2:] # definition list - definition is multiple words
		definition = ' '.join(map(str, definition_ls)) # turn definition_ls into a string
		insert_command = "INSERT INTO Vocab VALUES (%d, '%s', '%s', '%s');" % (n, word, part, definition) # predefined string for sql usage
		try:
			exc.execute(insert_command) # add stuff to database
		except sql.Error, e:
			print '%.2f: ERROR on \'%s\' (%d/5014): %s' % (time()-t0, word, n, e.args[0]) # print error message
			sys.exit(1)
		print '%.2f: SUCCESS on \'%s\' (%d/5014)' % (time()-t0, word, n) # print success message
		n+=1 #increment loop counter
	# end of for loop
	conn.commit()
# end of main()

if __name__ == '__main__': # this portion of code is executed when program starts
	main() # call the main() function
# end of if
