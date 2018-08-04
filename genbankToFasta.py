from Bio import SeqIO
from BCBio import GFF

file_name = "BGC0000729.1.cluster001"
file_type = "genbank"

def main():
    seq_record = SeqIO.parse(file_name+".gbk",file_type)
    fasta_handle = open(file_name+".fasta","w")
    SeqIO.write(seq_record,fasta_handle,"fasta")
    fasta_handle.close()

    seq_record2 = SeqIO.parse(file_name+".gbk",file_type)
    gff_handle = open(file_name+".gff3","w")
    GFF.write(seq_record2,gff_handle)
    gff_handle.close()

main()

