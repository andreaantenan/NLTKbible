import nltk
import os
import sys
import re
import operator
import string

#locate myself in correct path
files = os.listdir("/Users/andreaantenan/Desktop/cs195/NLTKbible/LastSupper")


# command line should look like python PrintText.py bookofbible.txt
file = sys.argv[1] #Matt.txt, John.txt, etc.
file2= sys.argv[2] #BOOKmatt.txt, BOOKjohn.txt, etc.

#turns file into corpora and text object
from nltk.corpus import PlaintextCorpusReader
corpus_root = "/Users/andreaantenan/Desktop/cs195/NLTKbible/LastSupper" # "." means the existing directory I am in#
file = PlaintextCorpusReader(corpus_root, file)
file = nltk.Text(file.words()) #creates text object#

#incorporates stopwords to file
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('bible.txt')
searchtext = [word for word in file if word.lower() not in stopwords]

#turns file2 into corpora and text object
from nltk.corpus import PlaintextCorpusReader
corpus_root = "/Users/andreaantenan/Desktop/cs195/NLTKbible/LastSupper" # "." means the existing directory I am in#
file2 = PlaintextCorpusReader(corpus_root, file2)
file2 = nltk.Text(file2.words()) #creates text object#

#incorporates stopwords into file2
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('bible.txt')
searchbook = [word for word in file2 if word.lower() not in stopwords]


#Figure out collocations to get a gist of the text#

print "\nMost common collocations in text:"
collocations=file.collocations()
print collocations 

#Print plot of 20 most common words#
fdist1 = nltk.FreqDist(searchtext)

print "\nPrinting frequency plot of most common words"

fdist1.plot(20, cumulative=False)

#Print list of all of frequently used words
top=[]

print "\nMost Frequent Terms"
for (key,value) in sorted(fdist1.items(), key=operator.itemgetter(0)):
	if value > 2:
		top.append(key)
		print key,":",value

#concordance
print "\nConfiguring concordance of most frequently used words"
for word in top:
	print " "
	print file.concordance(word,150,lines=all)

#similar

	
print "\nWords similar to most used words throughout book:"
for word in top:
	print word, ":", file2.similar(word)
	print " "
 

#Dispersion plots of top10 and collocations#
print "\nProcessing dispersion plot of ten most common words..."
print file.dispersion_plot(top)


sys.exit()













