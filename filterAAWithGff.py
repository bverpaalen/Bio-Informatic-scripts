#!/usr/bin/env python3
import sys
from Bio import SeqIO

def main(gffFile,aaFile):
    genesToKeep = GenesToKeep(gffFile)
    filterGenes(aaFile,genesToKeep)

def GenesToKeep(gffFile):
    genesToKeep = []
    readFile = open(gffFile,'r')
    for line in readFile:
        line = line.replace("\n","")
        if 'start gene' in line:
            splitLine = line.split(" ")
            gene = splitLine[-1]
        elif '% of transcript supported by hints (any source):' in line:
            splitLine = line.split(" ")
            hints = float(splitLine[-1])
            if hints > 0:
                genesToKeep.append(gene)
    return genesToKeep

def filterGenes(aaFile,genesToKeep):
    #readFile = open(aaFile,'r')
    recordToKeep = []
    keptGenes = 0
    for record in SeqIO.parse(aaFile,"fasta"):
        geneId = record.id.split('.')[0]
        if geneId in genesToKeep:
            keptGenes = keptGenes + 1
            recordToKeep.append(record)
    SeqIO.write(recordToKeep,"./output.fasta",'fasta')
    print(keptGenes)
    print(str(len(genesToKeep)))

main(sys.argv[1],sys.argv[2])
