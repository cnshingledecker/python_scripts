# -*- coding: utf-8 -*-
"""
A script that compares added species to current list of species and gives those
species that have yet to be added

@author: cns
"""

import reader


kida_file = 'gas_reactions.in'
kida_species = reader.reader(kida_file)
outfile = 'network_gas_species.txt'
outf = open(outfile,'w')
for item in kida_species:
    outf.write(item + '\n') 
    
outf.close()
print 'Finished script'