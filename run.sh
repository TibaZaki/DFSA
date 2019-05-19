#!/bin/sh
# Author: Tiba Zaki Abdulhameed April 11,2018 Western Michigan University/Al-Nahrain University
	#PLEASE CHANGE IraqiDialectToyCorpus.txt , MSAToyCorpus.txt TO YOUR CORPUS FILE NAME
	echo Starting dialect Fast Stemming Algorithm DFSA	
	c1=IraqiDialectToyCorpus.txt #this file is prepared coupus 
	c2=MSAToyCorpus.txt
	echo "Start counting"
        # create vocabulary files 
        python3 count_word.py $c1 
	python3 count_word.py $c2

	echo "cleanup the vocabulary words"
					
	sed -i '/^$/d' ${c1}.w  #we need to delete empty lines if exsit 
	sed 's/\r//' $c1 >$c1.r #deleting \r character
	sed  -e 's/إ/ا/g' -e 's/أ/ا/g' -e 's/آ/ا/g' $c1.r > $c1.hamz #normalize all kinds of Alef letter أشهر ,اشهر إغتيال ,اغتيال توحيد شكل الهمزه 
	 
	python3 DFSA.py $c1.hamz $c2.w $c1.w $c1.cleanedPre

        rm $c1.r $c1.hamz $c2.w $c1.w 
	echo cleaning dialect specific prefixes is completed successfuly
	
