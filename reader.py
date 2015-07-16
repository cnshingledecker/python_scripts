# -*- coding: utf-8 -*-
"""
This script compares the species in a list of reactions with the KIDA
database files and prints a list of species not in the network

@author: cns
"""
def reaction_compare(newfile,oldfile):
    inf1 = open(newfile,'r')

    outfile1 = 'redundent_' + newfile     
    outfile2 = 'not_redund_' + newfile
    
    out1 = open(outfile1,'w')
    out2 = open(outfile2,'w')

    words1 = []
    words2 = []



    duplicates = []
    nodup = []
    reactions = []
    
    inf2 = open(oldfile,'r')
    for line2 in inf2:
        react2 = []
        words2 = line2.split(' ')
        for word2 in words2:
            if word2 not in ['',' ']:
                react2.append(word2)
    
        react2 = react2[0:4]
        reactions.append(react2)
    inf2.close()

    for reaction in reactions:
        print reaction

    for line1 in inf1:
        react1 = []
        words1 = line1.split(' ')
        for word1 in words1:
            if word1 not in ['',' ']:
                react1.append(word1)
          
        react1 = react1[0:4]
        if react1 not in reactions:
            nodup.append(line1)
            out2.write(line1) 
        else:
            duplicates.append(line1)
            out1.write(line1)


    print len(duplicates),' redundant reactions found.'
 
    inf1.close()
    out1.close()
    out2.close()
    return nodup 

    


def reader(filename):
    
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
    outfile = '/home/cns/Dropbox/cyanopolyyne/species_' + filename
    outf = open(outfile,'w')             
    
    
    outlist = []
    for word in species:
        switch=0
        for letter in word:
            if letter in goodletter:
                switch = switch + 1
        if switch > 0:
            outf.write(word + '\n')
            outlist.append(word)
        for letter in word:
            if letter in noletter:
                switch = switch + 1
        if switch == 0:
            try:
                int(word)
            except:
                if word.strip() != '':
                    outf.write(word + '\n')
                    outlist.append(word)           
    outf.close()
    return outlist
    
    
    
def listcompare(list1,list2):
    difference = []
    for item in list1:
        if item not in list2:
            difference.append(item)
    return difference   
 

           
def listify(file):
    infile = file
    inf = open(infile, 'r')
    list = [inf.read().strip('\n')]  
    return list
    
def xor(list1, list2):
    outputlist = []
    list3 = list1 + list2
    for i in range(0, len(list3)):
        if ((list3[i] not in list1) or (list3[i] not in list2)) and (list3[i] not in outputlist):
             outputlist[len(outputlist):] = [list3[i]]
    return outputlist
    
    
def scrubber(filename,nolist):
    infile = filename
    inf = open(infile,'r')
    outfile = 'scrubbed_' + filename
    outf = open(outfile,'w')

    lines = inf.readlines()
    outlines = []
    for line in lines:
        switch = 0
        words = line.split(' ')
        for word in words:
            if word in nolist:
                switch = switch + 1
        if switch == 0:
            outf.write(line)
            outlines.append(line)
            
    inf.close()
    outf.close()
    return outlines
    
def renumber(filename,initnum):
    infile = filename
    inf = open(infile,'r')
    outfile = 'renumbered_' + filename
    outf = open(outfile,'w')
#    outf.write(inf.readline())

    lines = inf.readlines()
    for line in lines:
        print line[167:171] 
        newline = line[:167] + str(initnum) + line[171:]
        outf.write(newline)
        initnum = initnum + 1

    inf.close()
    outf.close() 
    
def noarrow(filename):
    infile = filename
    inf = open(infile,'r')
    outfile = 'noarrow_' + filename
    outf = open(outfile,'w')

    lines = inf.readlines()
    for line in lines:
        print line[34:36] 
        newline = line[:33] + ' ' + line[37:]
        outf.write(newline)

    inf.close()
    outf.close() 

if __name__ == '__main__':
    new_reactions = 'gas_species.in'
    print 'Now calling reader module on species file:'
    master_species = reader(new_reactions)
    
    
    kida_file = 'gas_reactions.in'
    print 'Now calling reader on reactions file'
    kida_species = reader(kida_file)

    
    print 'Now comparing two lists'
    diff_list = listcompare(master_species,kida_species)
    print 'The species not in KIDA are:'
    print diff_list

    print 'Now reversing the compare order'
    diff2 = listcompare(kida_species,master_species)
    print 'The results are:'
    print diff2
    
#    print 'The species in the new master file are:'
#    print master_species
    
#    compList = ['HC11N','C11HN+','C11H2N+','C11H+','C11H3N+','C11N','C11N+','C10H4N+','CH3C9N']
    compList = ['C11N','C11N+','C11HN+','C11H2N+','HC10N','NC10N','HC9N','HC9N+','H3C9N+','HC11N','C11H3N+','C10H4N+','CH3C9N','H3C8NH+']
    print 'now comparing lists:'            
    not_added = listcompare(diff_list,compList)
    print 'The species that have not been added are:'
    print not_added
    
