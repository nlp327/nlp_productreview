#code to remove the stop words and special characters from input data

import re
import subprocess


stopwordsfile = input("stop words file name : ")


stopwords=[]
for i in open(stopwordsfile):
    i=re.sub('\n', '', i)
    stopwords.append(i.lower())

inputfile = input("input file name : ")
outputfile = input("output file name : ")
f1=open(outputfile,'w')
for f in open(inputfile):
#check for special characters 
    f=re.sub('[^A-Za-z\-\s\+\']+',' ',f)
    f=re.sub('\s+', ' ', f)
    f=re.sub('\'','',f)
    f=re.sub('\"','',f)
    words=f.split(' ')
    for i in words:
        i=i.lower()
#check for stop words
        if i not in stopwords:
            f1.write(i + ' ')
    f1.write('\n')
print("Check the output file")

proc = subprocess.Popen(['gedit', outputfile ])

