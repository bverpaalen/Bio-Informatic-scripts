#Author: Brent Verpaalen
#Function: Takes a blast result and gives back all the different species that came from that blast result
#Date: 15-3-2017

#Before using:
#pathToFiles should be the path to the file(s) you want to open
#filesToOpen should be the file(s) you want to open, regex can be used
#fileToOpenExtension should be the extension of the file you want to open
#yourSpecie should be the specie you don't want in the output, can be empty

#Edits:


from Bio import SeqIO
import glob

pathToFiles="/home/bverpaalen/Desktop/"
filesToOpen = "SPLIT_*.fasta_results"
fileToOpenExtension = ".txt"
yourSpecie = "Amborella trichopoda"

def main():
    files = getFiles()
    for fileToOpen in files:
        blastResult = getFile(fileToOpen)
        speciesInBlastResult = getSpeciesWithId(blastResult)
        writeToFile(speciesInBlastResult,fileToOpen)
    print("Specie filtering done!\nResult at "+pathToFiles+filesToOpen+".species.txt")

#Gets the different files, regex can be used here
def getFiles():
    files = glob.glob(pathToFiles+filesToOpen+fileToOpenExtension)
    return files
    
def getFile(fileToOpen):
    blastResult = open(fileToOpen,'r');
    return blastResult

#Loops through the file
#Takes the contigName/Id and the specie
#Looks if the specie is already in the list or if it is your specie
#If not appends to the list
def getSpeciesWithId(blastResult):
    speciesInBlastResult=[]
    
    for line in blastResult:        
        splicedLine = line.split("\t")
        contigId=splicedLine[0]
        specie=splicedLine[13]

        if specie not in speciesInBlastResult and yourSpecie is not "" and yourSpecie not in specie:
            speciesInBlastResult.append(specie)

        elif specie not in speciesInBlastResult and yourSpecie is "":
            speciesInBlastResult.append(specie)
            
    blastResult.close()    
    return speciesInBlastResult

#Writes result to file
def writeToFile(speciesInBlastResult,fileToOpen):
    outputFile=open(fileToOpen+".species.txt","w")
    for specie in speciesInBlastResult:
        outputFile.write(specie+"\tRemove:y/n")
        outputFile.write("\n")
        
main()
