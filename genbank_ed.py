
#!/usr/bin/env python
# coding: utf-8

#In[]
from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

# adapted from: https://biopython.readthedocs.io/en/latest/chapter_blast.html
#example: result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")

#open a fasta file with a SINGLE query sequence (for now) [will try later with a 'multi_query.fasta']
record = SeqIO.read("solo_query.fasta", format="fasta")
print("got fasta")

#blast that sequence in the nucleotide database and store 50 results as 'result_handle' which is by default in XML
result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)

results = NCBIXML.read(result_handle)
print("got blast results")

# Make list of genbank IDS for blast results #

#save result output as an XML file so that you can check the results
with open("solo_query_blast2.xml", "w") as out_handle:
    out_handle.write(results())
    result_handle.close()

print("wrote xml")

# In[]
#PARSE XML
#from https://biopython.readthedocs.io/en/latest/chapter_blast.html#sec-parsing-blast

#blast_record = NCBIXML.read(result_handle) #can also use NCBI.parse() if you have multiple fasta query results

# USING A TEST XML FILE because the blast results are very slow with this method...
dummy_handle = open("test.xml", 'r')
dummy_records = list(NCBIXML.parse(dummy_handle)) #can also make list

#store blast result IDs in list 'results_ID'
results_ID = []
for alignment in dummy_records[0].alignments:
    results_ID.append(alignment.accession)

print(results_ID[0:5])
    

#In[]
#GET GENBANK FILE FOR RESULTS
from Bio import Entrez
Entrez.email = 'curiousgeorge@ufl.edu'

open('dummy_results_gb.txt','w')
for gb_ID in results_ID:
    gb_handle = Entrez.efetch(db="nucleotide", id=gb_ID, rettype="gb", retmode="text",retmax=1)     
    local_file=open('dummy_results_gb.txt','a') #a = append mode
    local_file.write(gb_handle.read()) #add data to end of file

gb_handle.close()






# %%
