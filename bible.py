import nltk
import os
import operator

# Retrieve a file list#
files = os.listdir(".")
print "All the files in the directory"
#Starts a loop that prints the name of each file, #
#with the condition that it ends with ".txt"#
for file in files:
	if file.endswith(".txt"):
		print file

file_name = raw_input("Choose the file:")

print "The file that was chosen is {0}".format(file_name)

from nltk.corpus import PlaintextCorpusReader
corpus_root = "." # "." means the existing directory I am in
search_text = PlaintextCorpusReader(corpus_root, file_name)
search_text = nltk.Text(search_text.words()) #creates text object

keyword = raw_input("Specify word to search:")

search_text.concordance(keyword, 80, lines=30)



##NEW THING##
from nltk.corpus import PlaintextCorpusReader
corpus_root='.'
search_text=PlaintextCorpusReader(corpus_root,file_name)
search_text=nltk.Text(search_text.words())

#
from nltk.corpus import stopwords
stopwords=nltk.corpus.stopwords.words('english_copy')

search_text= [word for word in search_text if word.lower() not in stopwords]

#frequency distribution vocabulary list; fd is a dictionary#
fd=nltk.FreqDist(search_text)

print "\nFrequency Distribution of terms in",file_name
for (key,value) in sorted(fd.items(), key=operator.itemgetter(0)):
	if value > 100:
		print key, value




#add frequency distribution


#create separate working files for Genesis 1:1-2:4A (Priestly) and for Genesis 2:4B-3:25 (Yahwest)