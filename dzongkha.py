import nltk

#python code to read Dzongkha text file
from nltk.corpus import PlaintextCorpusReader
corpus_root='C:/Users/Arie Namgay/Documents/GitHub/Dzongkha'
wordlists = PlaintextCorpusReader(corpus_root, 'story.txt')
print(wordlists)
dzongkha=wordlists.words()
length=len(dzongkha)
print("The total no of words in the text is: %d" % length)
print("\n")
for index, item in enumerate(dzongkha):
	print(item, end=" "),
	if(dzongkha[index]=="}*"):
		print('\n')
print("\n")

