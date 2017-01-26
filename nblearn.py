import sys
import string
import os

from collections import Counter

trainFilePointer = open(sys.argv[1])
trainLabelsPointer = open(sys.argv[2])

allWordsList = []
vocabulary = []
reviewsMapping = {}
positiveMapping = {}
negativeMapping = {}
truthfulMapping = {}
deceptiveMapping = {}
for line in trainFilePointer:
    truncatedWordList = []
    allWordsList = line.split()
    for word in allWordsList:
        newWord = word.translate(None, string.punctuation)
        newWord.strip()
        if newWord != '':
            truncatedWordList.append(newWord)
    key = truncatedWordList.pop(0)
    reviewsMapping[key] = truncatedWordList
for key, value in reviewsMapping.items():
    vocabulary.extend(value)

for line in trainLabelsPointer:
    labels = line.split()
    key = labels[0]
    typeClass = labels[1]
    meaningClass = labels[2]
    if typeClass == "truthful":
        truthfulMapping[key] = reviewsMapping[key]
    else:
        deceptiveMapping[key] = reviewsMapping[key]
    if meaningClass == "positive":
        positiveMapping[key] = reviewsMapping[key]
    else:
        negativeMapping[key] = reviewsMapping[key]
print "Total reviews = " + str(len(reviewsMapping))
print "Truthful = " + str(len(truthfulMapping))
print "Deceptive = " + str(len(deceptiveMapping))
print "Positive = " + str(len(positiveMapping))
print "Negative = " + str(len(negativeMapping))
positiveProbability = float(len(positiveMapping))/float((len(reviewsMapping)))
negativeProbability = float(len(negativeMapping))/float((len(reviewsMapping)))
truthfulProbability = float(len(truthfulMapping))/float((len(reviewsMapping)))
deceptiveProbaility = float(len(deceptiveMapping))/float((len(reviewsMapping)))
print "Positive Probability = " + str(positiveProbability)
print "Negative Probability = " + str(negativeProbability)
print "Truthful Probability = " + str(truthfulProbability)
print "Negative Probability = " + str(negativeProbability)

# find the probabilities of the individual words here.

vocabulary = map(str.lower, vocabulary)
allWordsCount = Counter(vocabulary)
trimmedVocab = set(vocabulary)


positiveWordsList = []
for key in positiveMapping.keys():
    positiveWordsList.extend(positiveMapping.get(key))
positiveWordsList = map(str.lower, positiveWordsList)
trimmedPositiveWordList = set(positiveWordsList)
positiveWordListCount = Counter(positiveWordsList)

positiveWordsProbability = {}
for key in positiveWordListCount.keys():
    wordCount = positiveWordListCount[key]
    positiveWordsProbability[key] = float(wordCount + 1)/float((len(positiveWordsList) + len(trimmedVocab)))

negativeWordsList = []
for key in negativeMapping.keys():
    negativeWordsList.extend(negativeMapping.get(key))
negativeWordsList = map(str.lower, negativeWordsList)
negativeWordListCount = Counter(negativeWordsList)

negativeWordsProbability = {}
for key in negativeWordListCount.keys():
    wordCount = negativeWordListCount[key]
    negativeWordsProbability[key] = float(wordCount + 1)/float((len(negativeWordsList) + len(trimmedVocab)))


cwd = os.getcwd()
cwd += "\\nbmodel.txt"
outputFile = open(cwd, 'w')
outputFile.write("Number of reviews:" + str(len(reviewsMapping)))
outputFile.write("\nNumber of Positive Reviews:" + str(len(positiveMapping)))
outputFile.write("\nNumber of Negative Reviews:" + str(len(negativeMapping)))
outputFile.write("\n\nIndividual Probabilities")
outputFile.write("\n$$Positive$$")
for key, value in positiveWordsProbability.items():
    outputFile.write("\n" + key + ":" + str(value))

outputFile.write("\n$$Negative$$")
for key, value in negativeWordsProbability.items():
    outputFile.write("\n" + key + ":" + str(value))

outputFile.close()
print len(trimmedVocab)
print len(vocabulary)
