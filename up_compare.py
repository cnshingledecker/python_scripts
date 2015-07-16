# -*- coding: utf-8 -*-
"""
This script takes a list reactions for some species (given in a file) and another,
and compares them. For reactions that are not common to both, they are written
to an output file. 

@author: cns
"""

spec = 'HC9N'
file_end = '_reactions.txt'
infile2 = 'master_list_hc9n.txt'
infile1 = 'gas_reactions.in'
outfile = spec + '_upconverted_reacts_compare.txt'

# Read the contents of the first file into a list
with open(infile1) as inf1:
    lines1 = inf1.readlines()

first2 = []
for line in lines1:
    words = line.split(' ')
    for word in words:
        if word == '' or word == '->':
            words.remove(word)
    first2.append([words[0],words[1]])


first2_2 = []
with open(infile2) as inf2:
    lines2 = inf2.readlines()
    
for line in lines2:
    words = line.split(' ')
    for word in words:
        if word == '':
            words.remove(word)
    first2_2.append([words[0],words[1]])
    
    
for elements in first2_2:
    print elements
    
new_reacts = []
for i in range(len(first2_2)):
    if first2_2[i] not in first2:
        new_reacts.append(lines2[i])
        
for reacts in new_reacts:
    print reacts
        
inf1.close()

outf = open(outfile,'w')
for reacts in new_reacts:
    outf.write(reacts)
    
outf.close()