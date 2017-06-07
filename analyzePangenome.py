# Author: Brent Verpaalen
# Function: Analyze pangenome
# Date: 31-3-2017
# Edit:
# 26-4-2017 Added function to show smallest contig, Fixed bug where the last contig wasn't included, made code smaller
# Before:
# You need to use this script in your shell with the pangenome file as argument
# example: python analyzePangenome.py yourpangenome.fasta
# Known bugs:
# If give more than one file the second result has some information from the first one

import sys
global analyzeResult
global smallestContig
global output
global totalLengthNotReference
global totalNotReference
global smallContigs

analyzeResult = {}
smallestContig= 0
totalLengthNotReference = 0
totalNotReference = 0
smallContigs = 0
output = open('output','w')

#Loops through list of given paths and checks if the given arguments isn't the python file itself
def Main(listOfFiles):
    for filePath in listOfFiles:
        if filePath is not sys.argv[0]:
            result = analyzeFile(filePath)
            print(result)

#Opens file and looks through every line and analyzes line
#Uses a library to set variables
#Calculates average length of the pangenomic contigs
#Returns gathered information
def analyzeFile(filePath):
    fileToRead = open(filePath,'r')
    
    contigInformation = {}
    contigInformation['analyzeResult'] = {}
    contigInformation['headerIsReference'] = False
    contigInformation['header'] = ""
    contigInformation['scaffold'] = ""

    
    for line in fileToRead:
        lineIsHeader = isHeader(line)
        analyzeContig(line,lineIsHeader,contigInformation)
    analyzeContig(line,True,contigInformation)
    

    if totalLengthNotReference is not 0 and totalNotReference is not 0:        
        averageLengthNotReference = totalLengthNotReference / totalNotReference
    analyzeResult['totalScaffolds'] = totalNotReference
    analyzeResult['averageScaffoldLength'] = averageLengthNotReference
    analyzeResult['totalScaffoldsLength'] = totalLengthNotReference
    analyzeResult['smallestContig'] = smallestContig
    analyzeResult['Contigs > 100'] = smallContigs
    fileToRead.close()
    output.close()
    return analyzeResult

#Gets global used variables
#Checks if the line is a header
#Checks if the contig is smaller than x (could edit code to let this be a given variable)
#If the contig is smaller than the latest know smallest contig becomes the smallest contig
#If the header of the contig isn't a reference
#Adds 1 to found contigs
#Adds contig length to total know length
#Sets current line as header for the contig to come
#Checks if the header just set is a reference
#Resets scaffold
def analyzeContig(line,lineIsHeader,contigInformation):  
    global smallestContig
    global analyzeResult
    global output
    global totalLengthNotReference
    global totalNotReference
    global smallContigs
    
    if lineIsHeader:
        lengthScaffold = len(contigInformation['scaffold'])

        if lengthScaffold < 100:
            smallContigs = smallContigs + 1
        if lengthScaffold < smallestContig or smallestContig is 0:
            smallestContig = lengthScaffold
            
        if not contigInformation['headerIsReference'] and lengthScaffold is not 0:
            output.write(line)
            totalNotReference = totalNotReference + 1
            totalLengthNotReference = totalLengthNotReference + lengthScaffold
                
        contigInformation['header'] = line
        contigInformation['headerIsReference'] = isReference(contigInformation['header'])
        contigInformation['scaffold'] = ""
            
    elif not lineIsHeader and not contigInformation['headerIsReference']:
        contigInformation['scaffold'] = contigInformation['scaffold'] + line

#Checks if a line is a header by looking if it contains a >
def isHeader(line):
    if ">" in line:
        return True
    else:
        return False

#Checks if a line is a reference by looking for ref is in the line
#Switch the True and False if you want to know your total reference length
def isReference(line):
    if "ref" in line.lower():
        return True
    else:
        return False
#Adds given arguments from the commands line    
Main(sys.argv)
