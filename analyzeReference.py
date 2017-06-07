#Author: Brent Verpaalen
#Function: Analyzing reference
#Date: 26-4-2017
#Edit:
#Before:

import sys

def main(toAnalyze):
    for filePath in toAnalyze:
        result = analyzeFile(filePath)
        print(result)

def analyzeFile(filePath):
    referenceFile = open(filePath,'r')
    analyzeResult = {}
    scaffold = ""
    lengthScaffold = 0
    totalLengthScaffolds = 0
    totalScaffolds = 0

    for line in referenceFile:
        lineIsHeader = isHeader(line)

        if lineIsHeader:
            scaffoldLength = len(scaffold)

            if lengthScaffold is not 0:
                totalLengtScaffolds = totalLengthScaffolds + scaffoldLength
                totalScaffolds = totalScaffolds + 1
        else:
            scaffold = scaffold + line
    totalLengthScaffolds = totalLengthScaffolds + scaffoldLength
    totalScaffolds = totalScaffolds + 1
    analyzeResult["totalLengthScaffolds"] = totalLengthScaffolds
    analyzeResult["totalScaffolds"] = totalScaffolds

    return analyzeResult

def isHeader(line):
    if ">" in line:
        return True
    else:
        return False

    

main(sys.argv[1:])
