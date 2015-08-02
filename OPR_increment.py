# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:52:17 2015

@author: cns
"""

import random, os,subprocess

contFile = 'nls_control.d'
compFile = 'compile.sh'
exFile = 'nls.bash'
Nruns = 1
nH2 = 1E4
OPR_min = 1E-18
OPR_max = 1E-14
OPR_inc = (OPR_max - OPR_min)/Nruns


os.system('rm -rf OPR_run*')

temp_OPR = OPR_min
for i in range(0,Nruns):
    #Mkdir with os package
    temp_path = 'OPR_run_'+str(i)
    os.mkdir(temp_path)
    
    #Copy files into new directory
    cmd = 'cp * ./' + temp_path + '/'
    os.system(cmd)
        
    #Calculate new parameter values
    temp_OPR = temp_OPR + OPR_inc
    pH2 = nH2/(1+temp_OPR)
    oH2 = temp_OPR*pH2
    print temp_OPR,oH2,pH2
    print oH2 + pH2

    #Edit the input files
    infile = './' + temp_path + '/' + contFile
#    print infile
    i = 0
    inf =  open(infile,'r')
    lines = inf.readlines()
    inf.close()
#    outfile = './' + temp_path + '/new_' + contFile
    outf = open(infile,'w')
    for line in lines:
        i = i + 1
        if i == 73:
            newline = line[:14] + '%.6e' % oH2 + line[26:]
            newline = newline[:22] + 'D' + newline[23:]
            outf.write(newline)
        elif i == 74:
            newline = line[:14] + '%.6e' % pH2 + line[26:]
            newline = newline[:22] + 'D' + newline[23:]
            outf.write(newline)
        else:
            outf.write(line)
    outf.close()
    
#    #Change into new directory
#    os.chdir(temp_path)
#    
#    #Recompile with os
#    print 'Now recompiling'
#    cmd = './' + compFile
#    subprocess.call(cmd,shell=True)
#
#    #Run with os
#    print 'Starting Nautilus'
#    cmd = './'  + exFile
#    subprocess.call(cmd,shell=True)
#
#    #Change back into home directory
#    os.chdir('..')