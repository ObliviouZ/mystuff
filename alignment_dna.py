import os
import sys
os.chdir('C:/Users/berna/Desktop/Programação/python projects/Project')

# print(os.getcwd())

sequence_name = []
sequence_dna = []

with open('sequences.fasta', 'r') as f:
    fr = f.readlines()
    for line in fr:
        if line[0] == '>':
            sequence_name.append(line[1:-1])
        else:
            sequence_dna.append(line[0:-1])

print(sequence_dna)

# Working With sequences_dna only

# Finding biggest sequence, length and index
print(max(sequence_dna, key=len))
print((len(max(sequence_dna, key=len))))
index = sequence_dna.index(max(sequence_dna, key=len))
print(index)

dna_new_list = []

for dna in sequence_dna:
    if len(dna) < len(max(sequence_dna, key=len)):
        dna = dna + ((len(max(sequence_dna, key=len))-len(dna)) * '-')
        dna_new_list.append(dna)
    else:
        dna_new_list.append(dna)

print(dna_new_list)


# Convert list to dicrionary

for i in range(len(dna_new_list)):
    dna_dict = {i+1: dna_new_list[i] for i in range(len(dna_new_list))}

print(dna_dict)

# Allignment rules:
# GAP = -1
# UNMATCH = -1
# MATCH = +1

score = 0

# for dna, dna2 in zip(dna_new_list, dna_new):
#    for letter1, letter2 in zip(dna, dna2):
#        if letter1 == letter2:
#            score += 1
#        else:
#            score -= 1

print(score)
print(sys.version)
