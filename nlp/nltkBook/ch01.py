# List of materials
# -----------------
# text1: Moby Dick by Herman Melville 1851
# text2: Sense and Sensibility by Jane Austen 1811
# text3: The Book of Genesis
# text4: Inaugural Address Corpus
# text5: Chat Corpus
# text6: Monty Python and the Holy Grail
# text7: Wall Street Journal
# text8: Personals Corpus
# text9: The Man Who Was Thursday by G . K . Chesterton 1908

from __future__ import division
from nltk.book import *

print text1.concordance("monstrous")
#prints every occurrence of word monstrous in moby dick in context

print text1.similar("monstrous")
print text2.similar("monstrous")
#prints words used in similar range of contexts (this is a magical function)

text2.common_contexts(['monstrous', 'very'])
#prints shared contexts by words in list

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
#occurance plot of a list of words and how many words into text it is

len(set(text1))/len(text1)
#lexical diversity

f = FreqDist(text1)
print f
#prints frequency distribution of most recurring words

f.plot(50, cumulative=True)
#cumulative distro graph of 50 most recurring words

#'A collocation is a sequence of words that occur together unusually often.'
text4.collocations()
#prints collocations