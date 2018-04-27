##Paragraph reader that gives you info on the word and sentence content of given paragraph##

import re

f = open('paragraph.txt','r')

paragraph = str(f.read())
AllSentences = re.split('[.?!]+', paragraph)        #removing full stop punctiation to separate out sentences       
NoPunct = []
for sentence in AllSentences:
    if not sentence:
        AllSentences.remove(sentence)
    else:
        NoPunct = NoPunct + re.split('[,;:"-]+',sentence)  #removing non-stop punctuation and punctuation at end of paragraph


AllWords = []                                              #removing spaces
for phrase in NoPunct:
    AllWords = AllWords + phrase.split()

Letters = []
for word in AllWords:
    for i in range(len(word)):
        Letters = Letters + [word[i]]

NumWords = len(AllWords)
NumSentences = len(AllSentences)
AvgSenLen = float(NumWords/NumSentences)
AvgWordLen = float(len(Letters)/NumWords)

print("Number of Words:  " + str(NumWords))
print("Number of Sentences:  " + str(NumSentences))
print("Average Letter Count:  " + str(AvgWordLen))
print("Average Sentence Lenght:  " + str(AvgSenLen))

f.close()
