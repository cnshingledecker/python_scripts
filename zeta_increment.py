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
zeta_min = 1E-18
zeta_max = 1E-14
zeta_inc = (zeta_max - zeta_min)/Nruns


os.system('rm -rf zeta_run*')

temp_zeta = zeta_min
for i in range(0,Nruns):
    #Mkdir with os package
    temp_path = 'zeta_run_'+str(i)
    os.mkdir(temp_path)
    
    #Copy files into new directory
    cmd = 'cp * ./' + temp_path + '/'
    os.system(cmd)


        
    #Calculate new parameter values
    temp_zeta = temp_zeta + zeta_inc

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
        if i == 30:
            print line
            newline = line[:14]+'%1.3e ' % temp_zeta + line[24:]
            newline = newline[:19] + 'D' + newline[20:]
            print newline
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