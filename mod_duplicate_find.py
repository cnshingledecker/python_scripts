# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:10:09 2015

@author: cns
"""

list1 = [[1,2],[3,4],[4,5]]
list2 = [[6,7],[8,9],[4,5]]
list3 = []

for thing1 in list1:
    if thing1 in list2:
        print thing1,' is a duplicate'
    else:
        list3.append(thing1)
        
print 'The non-duplicated items are:'
print list3

infilename = 'carbon_master.txt'
outfilename = 'nodup_' + infilename

infile = infilename
outfile = outfilename
outfile2 = 'duplicate_carbon_rxns.txt'

inf = open(infile,'r')
inf.readline()
outf = open(outfile, 'w')
out2 = open(outfile2,'w')

lines = []
outlines = []
duplicates = []
#for line in inf:
#    words = line.split(' ')
#    lines.append(words)
    
for line in inf:
    if line in outlines:
        out2.write(line)
    else:
        outlines.append(line)
        outf.write(line)
    
#print outlines[1]
#for outline in outlines:
#    outf.write(outline)
            
inf.close()
outf.close()
out2.close()