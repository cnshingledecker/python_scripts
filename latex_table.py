# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:09:14 2015

@author: cns
"""
import Table
fout = open('mytable.tex','w')
t = Table.Table(3, justs='lrc', caption='Awesome results', label="tab:label")
t.add_header_row(['obj', 'X', '$\\beta$'])
col1 = ['obj1','obj2','obj3']
col2 = [0.001,0.556,10.56]   # just numbers
col3 = [0.12345,0.12345,0.12345]
t.add_data([col1,col2,col3])
t.print_table(fout)
fout.close()
