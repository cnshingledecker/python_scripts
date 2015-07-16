# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:10:09 2015

@author: cns
"""
import sys

infilename = sys.argv[1] 
outfilename = 'nodup_' + infilename

infile = infilename
outfile = outfilename
outfile2 = 'duplicate_' + infilename

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
#        print line,' is a duplicate.'
        out2.write(line)
    else:
        outlines.append(line)
        outf.write(line)
    
#print outlines[1]
#for outline in outlines:
#    outf.write(outline)
            
print len(duplicates),' duplicate reactions found.'

inf.close()
outf.close()
out2.close()
