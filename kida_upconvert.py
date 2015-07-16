# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 21:32:22 2015

@author: cns
"""
import string, shutil,sys
inspecies = sys.argv[1]
outspecies = sys.argv[2]
path = '/home/cns/Dropbox/cyanopolyyne/'
infilename = inspecies + '_gas_reactions.txt'
outfilename = outspecies + '_upconverted_gas_reactions.txt'

infile = infilename
outfile = outfilename
inf = open(infile,'r')
outf = open(outfile, 'w')
shutil.copy(infile,outfile)
wordlist = []
newlist = []
noword = [' ','logn','','->','H','H+','H2','H3+','C','C+','C-','CN','e-','CRP',
          'Photon','S-','CCH','OH','HCO+','H-','N','CO','O','O-','OH-','He',
          'He+','CN-','S','Fe']
           
nums = ['5','6','7','8','9','10','11']

for line in inf:
    words = line.split(' ')
    for word in words:
        try:
            testvar = float(word)
        except ValueError:
            if word not in noword and word not in wordlist:
                for num in nums:
                    if num in word:
                        tempvar = word
                        newword = string.replace(tempvar, num, str(int(num)+2))
                        while True:
                          print 'Change:',tempvar,'to:',newword
                          invar = raw_input('y/n: \n')
                          if invar == 'y':                        
                            newlist.append(newword)  
                            wordlist.append(word)
                            break
                          elif invar == 'n':
                            print 'word not changed.'
                            break
inf.close()


# Find and replace old species with upconverted ones

newdict = dict(zip(wordlist,newlist))


def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
    
data = open(infile).read()
newdata = replace_all(data,newdict)


outf.write(newdata)
outf.close()


# Find out which species are not in the network

sp_list = []
infile = '/home/cns/Dropbox/nautilus_test/nautilus/example_simulation/gas_species.in'
inf = open(infile, 'r')

for line in inf:
    words = line.split(' ')
    sp_list.append(words[0])
    
outfile = outspecies + '_inlist.txt'
outf = open(outfile,'w')
outf.write('Species not in the network are:\n')
for word in newlist:
    if word not in sp_list:
        outf.write(word + '\n')
outf.close()

outf = open(outfile,'a')
outf.write('Species in the network are:\n')
for word in newlist:
    if word in sp_list:
        outf.write(word + '\n')
outf.close()
