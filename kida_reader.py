# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 21:42:16 2015

This is a script that reads a KIDA reactions file and writes all reactions 
involving some specified reactants to a file. 

@author: Christopher N. Shingledecker, University of Virginia
"""
import sys
# The species to look for in the file. Note: it has to be the same case as in 
# the kida file.
species = sys.argv[1]
infilename = 'gas_reactions.in'
outfilename = species + '_gas_reactions.txt'

infile = infilename
outfile = outfilename

inf = open(infile,'r')
inf.readline()
outf = open(outfile, 'w')

for line in inf:
    words = line.split(' ')
    for word in words:
        if word == species:
            outf.write(line)
            
inf.close()
outf.close()
        


