# -*- coding: utf-8 -*-
"""
This script scrubs a file of reactions containing certain species

@author: cns
"""

import reader

new_reactions = 'total_master.txt'


scrub_list = ['C12','C12+','C12-']
print 'Now scrubbing reaction file:'
outLine = reader.scrubber(new_reactions,scrub_list)
