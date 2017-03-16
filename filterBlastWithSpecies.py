#Author: Brent Verpaalen
#Function: Looks if blastResult are specific kingdom with a file with all the species of the kingdom
#Date: 15-3-2017
#Before use:
#kingdomFileName: File with all the species of specific kingdom you want to keep
#pathToFiles: Path to the files you want to filter
#filesToOpen: Files name(s) you want to open, regex can be used
#fileToOpenExtension: Extension of the files you want to open

import glob

kingdomFileName="All_plant_genus_list_formatted.txt"
pathToFiles="/home/bverpaalen/Desktop/"
filesToOpen="SPLIT_*.fasta_results"
fileToOpenExtension=".txt"

def Main():
    files = getFiles()
    speciesInKingdom = getSpeciesKingdom()
    
    for blastResult in files:
        print("Opening: "+blastResult)
        checkFileForKingdom(blastResult,speciesInKingdom)
        
    print("Done!")

#Searches for files on the given path,Regex can be used        
def getFiles():
    files = glob.glob(pathToFiles+filesToOpen+fileToOpenExtension)
    return files

#Reads the file with all the species of a kingdom
def getSpeciesKingdom():
    speciesInKingdom = []
    kingdomFile = readFile(kingdomFileName)
    
    for line in kingdomFile:
        line = line.replace("\n","")
        speciesInKingdom.append(line)
        
    kingdomFile.close()
    return speciesInKingdom

def readFile(fileToOpen):
    openFile = open(fileToOpen,'r');
    return openFile

def writeFile(fileToOpen):
    openFile = open(fileToOpen,'w');
    return openFile

#Opens the blast results
#Per line looks if the specie is in the kingdom
#Only lookes at the first blast result of a contig
#If line specie is in kingdom puts the line in file.kingdomSpecific.extension
#If line specie is not in kingdom puts the line in file.removed.extension
def checkFileForKingdom(fileToOpen,speciesInKingdom):
    idsAlreadyHit = []
    removedLines = 0
    notRemovedLines = 0
    
    fileToOpenName = fileToOpen.replace(fileToOpenExtension,"")
    
    removed = writeFile(fileToOpenName+".removed"+fileToOpenExtension)
    outputFile = writeFile(fileToOpenName+".kingdomSpecific"+fileToOpenExtension)
    openFile = readFile(fileToOpen)
    
    for line in openFile:
        hit = False
        noHit = False
        i = 0

        lineSplit = line.split("\t")
        lineId = lineSplit[0]
        lineSpecie = lineSplit[13]

        if lineId in idsAlreadyHit:
            hit = True
        
        while(not hit and not noHit):
            specie = speciesInKingdom[i];
            
            if i+1==len(speciesInKingdom):
                noHit = True
                
            elif specie in line:
                hit = True
                #print("hit: "+specie)
                #print("id: "+lineId)
                outputFile.write(line)
                idsAlreadyHit.append(lineId)
                notRemovedLines = notRemovedLines + 1
                
            i = i+1
            
        if(noHit):
            #print("Removed: "+lineSpecie)
            #print("id: "+lineId)
            idsAlreadyHit.append(lineId)
            removed.write(line)
            removedLines = removedLines + 1
                              
    outputFile.close()
    openFile.close()
    removed.close()
    print("Total removed lines: "+str(removedLines))
    print("Total kept lines: "+str(notRemovedLines))
            

Main()
