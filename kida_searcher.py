# -*- coding: utf-8 -*-
"""
This script compares the species in a list of reactions with the KIDA
database files and prints a list of species not in the network

@author: cns
"""

def reader(filename,array):
    
    infile = '/home/cns/Dropbox/cyanopolyyne/' + filename 
    inf = open(infile,'r')
    
    species = []
    noword = [' ','logn','','->','H','H+','H2','H3+','C','C+','C-','CN','e-','CRP',
              'Photon','S-','CCH','OH','HCO+','H-','N','CO','O','O-','OH-','He',
              'He+','CN-','S','Fe']
    for line in inf:
        words = line.split(' ')
        for word in words:
            if word not in species and word not in noword:
                species.append(word)
             
    goodletter = ['C','H','O','N','S','P']
    noletter = ['e']
    inf.close()            
    outfile = '/home/cns/Dropbox/cyanopolyyne/species_list_' + filename
    outf = open(outfile,'w')             
    outf.write('Species not in the network are:\n')
    
    array = []
    for word in species:
        switch=0
        for letter in word:
            if letter in goodletter:
                switch = switch + 1
        if switch > 0:
            outf.write(word + '\n')
            array.append(word)
        for letter in word:
            if letter in noletter:
                switch = switch + 1
        if switch == 0:
            try:
                int(word)
            except:
                if word.strip() != '':
                    outf.write(word + '\n')
                    array.append(word)
        
            
    outf.close()
    return array

