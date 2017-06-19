#!/usr/bin/env python3
import sys
from Bio import SeqIO

def main(genomeFilePath):
    sequences = GetGenomeFromFile(genomeFilePath)
    information = InformationGenome(sequences)

def GetGenomeFromFile(genomeFilePath):
    sequences = []
    for record in SeqIO.parse(genomeFilePath,'fasta'):
        sequences.append(record.seq)
    return sequences

def InformationGenome(sequences):
    genomeLength = 0
    for sequence in sequences:
        genomeLength = genomeLength + len(sequence)
    print(str(genomeLength/1000000))

main(sys.argv[1])
