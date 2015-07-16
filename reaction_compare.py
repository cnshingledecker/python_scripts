# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:49:32 2015

@author: cns
"""

import sys,reader

newf = sys.argv[1]
oldf = sys.argv[2]

reader.reaction_compare(newf,oldf)
