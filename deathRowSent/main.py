import codecs

afinn = {}
file = open('AFINN-111.txt')

for line in file:
    key, value = line.split('\t')
    val = (int)(value.replace("\n", ""))
    afinn[key] = val

def sentimentCalc(sentence):
    arr = sentence.split(" ")
    sent = 0
    for word in arr:
        if word in afinn:
            sent += afinn[word]
    return sent

highest_score = 0
highest_sentence = ''
lowest_sentence = ''
lowest_score = 0

f = codecs.open('out.txt', 'r', 'utf-16')
f2 = open('data.txt', 'a')
for line in f:
    sent = sentimentCalc(line)
    f2.write(str(sent)+'\n')
    if sent > highest_score:
        highest_score = sent
        highest_sentence = line
    if sent < lowest_score:
        lowest_score = sent
        lowest_sentence = line

print 'highest sentence: ' + highest_sentence
print 'score '+ str(highest_score)
print 'lowest sentence: ' + lowest_sentence
print 'score '+ str(lowest_score)
