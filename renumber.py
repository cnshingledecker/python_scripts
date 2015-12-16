# -*- coding: utf-8 -*-
"""
This script calls the function that renumbers reactions in a nautilus compatible network 

@author: cns
"""

import reader,sys



new_reactions = sys.argv[1] 
startnum = int(sys.argv[2])

print 'No-arrowing reactions:'
filename = new_reactions
reader.renumber(filename,startnum)
#reader.noarrow(filename)

