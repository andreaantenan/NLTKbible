
from nltk.corpus import PlaintextCorpusReader
corpus_root='.'
search_text=PlaintextCorpusReader(corpus_root,file_name)
search_text=nltk.Text(search_text.words())


from nltk.corpus import stopwords
stopwords=nltk.corpus.stopwords('english')

search_text= [word for word in search_text if word.lower() not in stopwords]

#frequency distribution vocabulary list; fd is a dictionary#
fd=nltk.FreqDist(search_text)

print "\nFrequency Distribution of terms in",file_name
for (key,name) in fd.items():
	if value > 100:
		print key, value

