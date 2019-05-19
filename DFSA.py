#!/usr/bin/python3
# -*- coding: utf-8 -*-
import itertools
import collections
import sys 
import codecs
# author: Tiba Zaki Abdulhameed Jan 12,2018 Western Michigan University/Al-Nahrain University Iraq
# this program takes 4 argument
#1: dialect corpus to be morphologicaly processed
#2: MSA vocabulay file of words, each word on line
#3: Dialect vocabulary file of words, each word on line
#4: output file
# this additional dialect morphological processing is trying to expand the dialect-MSA intersection set

if(len(sys.argv)!=5):print('Arguments error ')
else:
		
	word_file=sys.argv[1] #input dialect corpus
	
	print('Starting Dialect Stemming DFSA')
	with codecs.open(word_file,'r','utf-8') as f:
		L= list(itertools.chain( line.split() for line in f)) #save the file as list of lines
	f.close()
	
	vocab_file=sys.argv[2]
	with codecs.open(vocab_file,'r','utf-8') as f:
		V=f.read().splitlines()
		
	f.close()
	#print(V)
	vocab2_file=sys.argv[3]
	with codecs.open(vocab2_file,'r','utf-8') as f:
		VI = f.read().splitlines()
		
	f.close()
	#print(VI)
	target = codecs.open(sys.argv[4], 'w','utf-8')# This is the output file "dialect specif morphologically analyzed 
	
	for line in L:#iterate through corpus
		newLine="";	
		for x in line:#iterate through words in line
			prefix='';			
			word=str(x);
			l=len(word);
				
			if len(word)>=5 and word.startswith('و') and (word[1:] in V or word[1:] in VI): # if the  و letter is external to the actual word
				word=word[1:];# extraxt first letter away from the word
				l=l-1;
				prefix='و+ '; 
			if len(word)>=5 and word.startswith('بهال'):
				word=word[4:];
				prefix=prefix+'ب+ هال+ ';
			if len(word)>=4 and word.startswith('بال'):
				word=word[3:];
				prefix=prefix+'ب+ ال+ ';
				
			if len(word)>=6 and word.startswith('ب')and (word[1:] in V or word[1:] in VI) and not word in V :# if it is in V then it is in the intersection and letter ب is original part of the word cause MADAMIRA was not able to split it
				word=word[1:];
				prefix=prefix+'ب+ ';
			
			#if not(word in V): # if word is not already in the intersection set
			if (word[3:] in V  or word[3:]in VI) and len(word)>=6: # check if the word has a prefix of 3 letters that is when splitted the word will be in the intersection set
				# for debuging target.write('ييييييييييييي');
				if word.startswith('هال'):
					word=word[3:];
					prefix=prefix+'هال+ ';
					
			if (word[2:] in V or word[2:]in VI) and len(word)>=5:	# check if the word has a prefix of 2 letters that is when splitted the word will be in the intersection set				
				
				if word.startswith('شد'):
					word=word[2:];
					prefix=prefix+'ش+ د+ ';
				elif word.startswith('ال'):
					word=word[2:];
					prefix=prefix+'ال+ ';
			if (word[1:] in V or word[1:]in VI) and len(word)>=5: # check if the word has a prefix of 1 letters that is when splitted the word will be in the intersection set
				
				if word.startswith('ش'):
					word=word[1:];
					prefix=prefix+'ش+ ';
				elif  word.startswith('حي')or word.startswith('حت') or word.startswith('حا'):
					word=word[1:];
					prefix=prefix+'ح+ ';
				elif word.startswith('د'):
					word=word[1:];
					prefix=prefix+'د+ ';
			#if str(x) != word:#processed
			newLine=newLine+prefix+word+' ';# accumilate words with its prefixes to form a line
		target.write("%s\n " %(newLine));
		
					
target.close()
