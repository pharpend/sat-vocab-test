#!/usr/bin/python

'''
sat_word_based_quiz.py

Copyright 2012 Peter Harpending.

Description:
Program that quizzes end user on SAT vocabulary. Asks nq questions.

Proposed Setup:
quiz calls sat_word_chooser. process1() function chooses a word, its answer, and four wrong answers. make_str() function formats a string to print on screen.
'''


from __future__ import division
from random import random, randint, shuffle
import sat_word_chooser as chuser
from sys import argv, exit
from math import trunc
from numpy import searchsorted



def save_output(f, q):
	f = open(f, 'w') # convert f into write file
	f.write(queue) # write f
	f.close() # gtfo
# end of saveoutput()

def ask_end_user(question, right_answer): 
	while True: # loop
		end_user_answer = raw_input(question) # ask the question
		if end_user_answer == 'x': exit(0) # if user wants to exit
		if end_user_answer == 'ans': # if user wants to cheat
			print( 'Correct answer is "%s"' % right_answer )# print correct answer
			continue # try again
		else: 
			print( 'Correct answer is "%s"' % right_answer )# print correct answer
			break
	# end of while loop
	return end_user_answer
# end of ask_end_user()

def process1(chuser_data): # first data formatter
	chuser_data = list(chuser_data)
	words = list(chuser_data[2]) # get the words list
	defs = list(chuser_data[1]) # get the defs list
	defs2 = defs
	
	q_word = words[0] # question word
	q_def = defs[0] # correct answer
	shuffle(defs2,random) # reshuffled answer
	
	return q_word, q_def, defs2	
# end of shuffle()	

def process2(q_num, data): # second data formatter
	question = data[0] # question
	all_ans = data[2] # all of the answers
	
	q_str = "\n--\n%d. What is the best word for '%s'?" % (q_num, question) # ask the question
	q_str += '\n'
	for ans_num in range(len(all_ans)):
		q_str += '*'
		q_str += '\t' # add tab
		q_str += all_ans[ans_num] # add the answer
		q_str += '\n'
	q_str += "Answer ('x' to exit): "
	return q_str
# end of process2

def main():
	try:
		queue = ''
		nq = int(raw_input('How many questions? '))	
		ncorrect = 0
		score_bracket = [59, 63, 66, 69, 73, 76, 79, 83, 86, 89, 93]
		grades = ['F','D-','D','D+','C-','C','C+','B-','B','B+','A-','A']
	
		for n in range(nq): # do this nq times
			word_jumble = chuser.main() # get a tuple of words and definitions
			processed_data_1 = process1(word_jumble) # select question and answer
			right_answer = processed_data_1[1] # get the right answer in its own variable
			all_answers = processed_data_1[2] # get all (shuffled) answers in their own variables
			processed_data_2 = process2(n+1, processed_data_1) # make question string
			eua = ask_end_user(processed_data_2, right_answer) # eua = end user answer
			iscorrect = right_answer == eua # check if answer is correct
			if iscorrect: ncorrect+=1 # add 1 to the number correct if correct
		
			percentage = trunc(100*(ncorrect/(n+1))) # truncated percentage
			grade_int = searchsorted(score_bracket, percentage) # integer representation of grade
			grade_letter = grades[grade_int] # letter representation of grade
		
			print( "(%d/%d) (%d percent) (%s)" % (ncorrect, n+1, percentage, grade_letter))
		# end of for loop
	
		percentage = trunc(100*(ncorrect/nq))
		grade_int = searchsorted(score_bracket, percentage)
		grade_letter = grades[grade_int]
		print ( 'You got %d correct out of %d (%d percent) (%s)' % (ncorrect, nq, percentage, grade_letter))
	except Exception, e: print "ERROR %s: %s" %(type(e), e.args[0])
	finally: raw_input('Press [Enter] to quit.')
# end of main()

if __name__ == '__main__':
	main()
