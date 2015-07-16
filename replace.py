# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 22:54:40 2015

@author: cns
"""
import re
output = "HC11N_reactions.txt"
file = "HC9N_reactions.txt"

wordlist = ['HC9N','CN',"C9H2N+"]
newlist = ['test1','test2','test3']

for i in range(0,len(wordlist)):
    o = open(output,"w")
    data = open(file).read()
    o.write( re.sub(wordlist[i],newlist[i],data) )
    o.close()