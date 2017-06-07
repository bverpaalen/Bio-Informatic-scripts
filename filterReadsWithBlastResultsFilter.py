#Author:Brent Verpaalen
#Function: Takes the result from the filterBlastWithSpecies.py and uses it to filter the orginal reads
#Date: 20-3-2017
#Edit:
#Before:
#pathToFiles should be the path where all your files are gathered
#filestoFilter should be all your orginal fasta files with the read data

import glob

pathToFiles="/home/bverpaalen/Desktop/blastTest/"
filesToFilter = "SPLIT_6.fasta"

def Main():
    print("Start running")
    files = getFiles(pathToFiles+filesToFilter)    
    for fileToOpen in files:
        kingdomSpecficFile = fileToOpen.replace(".fasta",".fasta_results.removed.txt")
        print("Filtering: "+fileToOpen+"\nWith :"+kingdomSpecficFile)
        blastFilter = getFiles(kingdomSpecficFile)
        idsToKeep = filterId(blastFilter[0])
        filteringReads(idsToKeep,fileToOpen)
    print("Done!")
        
        
def openReadFile(filePath):
    readFile = open(filePath,'r')
    return readFile

def createWriteFile(filePath):
    newWriteFile =open(filePath,'w')
    return newWriteFile

def getFiles(fileToSearch):
    files = glob.glob(fileToSearch)
    return files

#Takes the file from filterBlastWithSpecies.py and makes a list with all the read ids that should be kept
def filterId(fileToFilter):
    ids=[]
    toFilter = openReadFile(fileToFilter)
    for line in toFilter:
        splitLineOnTab = line.split("\t")
        idToKeep = splitLineOnTab[0]
        ids.append(idToKeep)
    toFilter.close()
    return ids

#Splits a file into a list with a specfic splitter 
def splitFile(fileToSplitPath,toSplitWith):
    fileToSplit = openReadFile(fileToSplitPath)
    totalFile = ""
    for line in fileToSplit:
        totalFile = totalFile + line
    splittedFile = totalFile.split(toSplitWith)
    fileToSplit.close()
    return splittedFile
        
#Loops through the read file and writes the ids (with read) that are in the idsToKeep list to a output file            
def filteringReads(idsToKeep,fileToOpen):
    i=0
    k=0
    allReadsIds = []
    outputFile = createWriteFile(fileToOpen.replace(".fasta",".filtered.txt"))
    
    readsFileSplit = splitFile(fileToOpen,">")
    
    for read in readsFileSplit:
        remove = False
        k = k + 1
        readSplit = read.split("\n")
        readId = readSplit[0]
        print(readId)
        allReadsIds.append(readId)
        for idToKeep in idsToKeep:
            if idToKeep in readId:
                remove = True
        if not remove:
            i = i +1
            outputFile.write(">"+read)
        
    print("Total reads: "+str(k))
    print("Reads kept: "+str(i))
    outputFile.close()
    
Main()
