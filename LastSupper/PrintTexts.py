cd desktop
cd cs195
cd LastSupper

import nltk


files = os.listdir(".")

print "All the files in the directory"

# Retrieve a file list#

for file in files:
	if file.endswith(".txt"):
		print file
		
		#Start a loop that prints the name of each file, #
		#with the condition that it ends with ".txt"#

file_name = raw_input("Choose the file:")

print "The file that was chosen is {0}".format(file_name)

from nltk.corpus import PlaintextCorpusReader
corpus_root = "." # "." means the existing directory I am in
search_text = PlaintextCorpusReader(corpus_root, file_name)
search_text = nltk.Text(search_text.words()) #creates text object
