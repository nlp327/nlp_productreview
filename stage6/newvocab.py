import re
import subprocess

outputfile = open("output.txt","r") 
outputfile1 = input("output file name : ") 
fovoc = open(outputfile1,"w")
unidict = {}
bidict = {}



outputfile = open("output.txt","r") 
for line in outputfile:
         words = line.split()
         for word in words[1:]:    #initialize the count of all words as 0 (unigrams)
           unidict.setdefault(word, 0)
           unidict[word] = unidict[word] + 1
	
         for i in range(1,len(words)-1):     #initialize the count of all words as 0 (bigrams)
                bigram = words[i] + ' ' + words[i+1]
                bidict.setdefault(bigram,0)
                bidict[bigram] = bidict[bigram] + 1

for word, count in unidict.items():	
	if(count >= 2): 	
		fovoc.write(word + "\n")

for word, count in bidict.items():	
	if(count >= 3): 	
		fovoc.write(word + "\n")

proc = subprocess.Popen(['gedit', outputfile1 ])
