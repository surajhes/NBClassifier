import sys,os


cwd = os.getcwd()

filePath = cwd + "\\" + sys.argv[1]
modelFile = open(filePath)
for line in modelFile:
    print line



