# Author: Tiba Zaki Abdulhameed April 11,2018 Western Michigan University/Al-Nahrain University
Example:
Iraqi contains
شدتاكل بهالليل

MSA contains 
تاكل ليل طويل
Iraqi.cleanedPre will be 
ش+ د+ تاكل ب+ هال+ ليل


Start running from run.sh
this will  
1- create vocabulary files 
2- Normalizing the Hamza form in Iraqi input corpus
3- Finally calls "python3 DFSA.py $c1.hamz $c2.w $c1.w $c1.cleanedPre"  To produced the stemmed Iraqi corpus, c1 is the Iraqi corpus file, c2 the MSA corpus file

Please cite the paper 
"Title: Wasf-Vec: Topology-Based Word Embedding for Modern Standard Arabic and Iraqi Dialect Ontology
Authors: TIBA ZAKI ABDULHAMEED, Department of Computer Science, College of Engineering and Applied Sciences,
 Western Michigan University, USA and Department of Computer Science, College of Science, Al-Nahrain University,Iraq
IMED ZITOUNI, Microsoft Research, USA
IKHLAS ABDEL-QADER, Department of Electrical and Computer Engineering, College of Engineering and Applied
Sciences, Western Michigan University, USA" 

