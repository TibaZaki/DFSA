#!/usr/bin/python3
import itertools
import collections
import sys
# Author: Tiba Zaki Abdulhameed April 11,2018 Western Michigan University/Al-Nahrain University Iraq
# This program takes 2 arguments; input file as Arabic corpus. output file is the vocabulary list with each word frequency 
# example of running command: python3 count_word.py toyCorpus.txt 
if(len(sys.argv)!=2):print('Arguments error ')
else:
	print('Hi count_word')	
	word_file=sys.argv[1] #input corpus
	print (word_file)
	
	with open(word_file) as f:
		L= list(itertools.chain( line.split() for line in f)) #save the file as list of lines
	L=list(itertools.chain(*L))# convert 2d list to 1d list
	f.close()
	
	counts = collections.Counter(L)
	vocabularyFileName=sys.argv[1]+".w"
	target = open(vocabularyFileName, 'w')#output vocabulary
	for item in counts:
		target.write("%s\n" %(item))
					
	target.close()


