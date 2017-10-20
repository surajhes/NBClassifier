import string
import sys
import math

modelFile = open("nbmodel.txt")
priorProbabilityParameters = {}
positiveWordMappingProbability = {}
negativeWordMappingProbability = {}
truthfulWordMappingProbability = {}
deceptiveWordMappingProbability = {}
n = 4
for i in range(n):
    line = modelFile.next().strip()
    splitLine = line.split(":")
    priorProbabilityParameters[splitLine[0]] = splitLine[1]

line = modelFile.next().strip()
strippedLine = line.strip("$$")
numberOfWordsInPositives = int(strippedLine.split(":")[1])
for i in range(numberOfWordsInPositives):
    line = modelFile.next().strip()
    splitLine = line.split(":")
    positiveWordMappingProbability[splitLine[0]] = splitLine[1]

line = modelFile.next().strip()
strippedLine = line.strip("$$")
numberOfWordsInNegatives = int(strippedLine.split(":")[1])
for i in range(numberOfWordsInNegatives):
    line = modelFile.next().strip()
    splitLine = line.split(":")
    negativeWordMappingProbability[splitLine[0]] = splitLine[1]

line = modelFile.next().strip()
strippedLine = line.strip("$$")
numberOfTruthfulWords = int(strippedLine.split(":")[1])
for i in range(numberOfWordsInNegatives):
    line = modelFile.next().strip()
    splitLine = line.split(":")
    truthfulWordMappingProbability[splitLine[0]] = splitLine[1]

line = modelFile.next().strip()
strippedLine = line.strip("$$")
numberOfDeceptiveWords = int(strippedLine.split(":")[1])
for i in range(numberOfWordsInNegatives):
    line = modelFile.next().strip()
    splitLine = line.split(":")
    deceptiveWordMappingProbability[splitLine[0]] = splitLine[1]


# from here read the line and calculate the class.
testFile = open(sys.argv[1])
allWordsList = []
positiveConditionalProbability = priorProbabilityParameters['positiveProbabilityLog']
negativeConditionalProbability = priorProbabilityParameters['negativeProbabilityLog']
truthfulConditionalProbability = priorProbabilityParameters['truthfulProbabilityLog']
deceptiveConditionalProbability = priorProbabilityParameters['deceptiveProbabilityLog']
classification = {}
for line in testFile:
    truncatedWordList = []
    positiveConditionLog = 0.0
    negativeConditionLog = 0.0
    truthfulConditionLog = 0.0
    deceptiveConditionLog = 0.0
    allWordsList = line.split()
    classes = []
    for word in allWordsList:
        newWord = word.translate(None, string.punctuation)
        newWord.strip()
        if newWord != '':
            newWord = newWord.lower()
            truncatedWordList.append(newWord)
    key = allWordsList[0]
    for individualWord in truncatedWordList:
        if positiveWordMappingProbability. has_key(individualWord):
            probability = float(positiveWordMappingProbability[individualWord])
            positiveConditionLog += probability
    for individualWord in truncatedWordList:
        if negativeWordMappingProbability. has_key(individualWord):
            negativeProbability = float(negativeWordMappingProbability[individualWord])
            negativeConditionLog += negativeProbability
    for individualWord in truncatedWordList:
        if truthfulWordMappingProbability. has_key(individualWord):
            truthfulProbability = float(truthfulWordMappingProbability[individualWord])
            truthfulConditionLog += truthfulProbability
    for individualWord in truncatedWordList:
        if deceptiveWordMappingProbability. has_key(individualWord):
            deceptiveProbability = float(deceptiveWordMappingProbability[individualWord])
            deceptiveConditionLog += deceptiveProbability
    positiveConditionLog += float(positiveConditionalProbability)
    negativeConditionLog += float(negativeConditionalProbability)
    truthfulConditionLog += float(truthfulConditionalProbability)
    deceptiveConditionLog += float(deceptiveConditionalProbability)
    if positiveConditionLog > negativeConditionLog:
        classes.append("positive")
    else:
        classes.append("negative")
    if truthfulConditionLog > deceptiveConditionLog:
        classes.append("truthful")
    else:
        classes.append("deceptive")
    classification[key] = classes

outputFile = open("nboutput.txt", 'w')
for key, value in classification.items():
    outputFile.write(key + " " + value[1] + " " + value[0]+"\n")
outputFile.close()



