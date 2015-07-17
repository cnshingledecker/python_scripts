# -*- coding: utf-8 -*-
"""
This script takes an input file of reactions and divides the alpha value
by some number specified by the user

@author: Christopher N. Shingledecker
@date:   2015-07-16
"""


filename = 'hh-h2hp-wrong-rates.in'
divide_by = 2 
form = '.3e'

def div_rate(filename,divNum):
    infile = filename
    inf = open(infile,'r')
    outfile = 'corrected_' + filename
    outf = open(outfile,'w')
#    outf.write(inf.readline()) #uncomment this line if there is a header line in the input file
    lines = inf.readlines()
    for line in lines:
        alpha = float(line[53:63])/divNum
        print line[53:63], "divided by", str(divNum), "equals %.3e" % alpha
        newline = line[:53] + "{:.3e}".format(alpha) + '  ' + line[64:]
        outf.write(newline)


    inf.close()
    outf.close() 
    bigE(outfile)
    
def bigE(filename):
    infile = filename
    inf = open(infile,'r')
    outfile = 'bigE_' + filename
    outf = open(outfile,'w')

    lines = inf.readlines()
    for line in lines:
        newline = line[:58] + 'E' + line[59:]
        outf.write(newline)

    inf.close()
    outf.close() 


print 'Dividing rates:'
div_rate(filename,divide_by)


