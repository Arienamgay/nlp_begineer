import nltk
import codecs
from nltk.corpus import PlaintextCorpusReader
corpus_root='C:/Users/Arie Namgay/Desktop/nlp/Dzongkha'
wordlists = PlaintextCorpusReader(corpus_root, 'story-Eng.txt')
print(wordlists)
dzongkha=wordlists.words()
for word in dzongkha:
    print(word),
