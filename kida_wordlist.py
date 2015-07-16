# -*- coding: utf-8 -*-
"""
This program creates a list of relevant words used in a kida file

@author: Christopher N. Shingledecker
"""

path = '/home/cns/Dropbox/cyanopolyyne/'
infilename = 'HC9N_reactions.txt'
infile = path + infilename

inf = open(infile,'r')

wordlist = []
noword = [' ','logn','','->','H','H+','H2','H3+','C','C+','C-','CN','e-','CRP',
          'Photon','S-','CCH','OH','HCO+','H-','N','CO','O','O-','OH-','He',
          'He+','CN-','S','Fe']
           
nums = ['6','7','8','9','10','11']

for line in inf:
    words = line.split(' ')
    for word in words:
        try:
            testvar = float(word)
        except ValueError:
            if word not in noword and word not in wordlist:
                for num in nums:
                    if num in word:
                        wordlist.append(word)
            
print wordlist