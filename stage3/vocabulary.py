import re
import subprocess


inputfile = input("input file name : ")

foinput = open(inputfile,"r")
outputfile = input("output file name : ") 
fovoc = open(outputfile,"w")
dict = {}

for eachline in foinput:
    words = eachline.split()
    for word in words[1:]:

#initialize the count of all words as 0

       dict.setdefault(word, 0)
       dict[word] = dict[word] + 1 


for word, count in dict.items():	
	if(count > 1): 	
		fovoc.write(word + "\n")

proc = subprocess.Popen(['gedit', outputfile ])
