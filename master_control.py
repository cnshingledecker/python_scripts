# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:52:17 2015

@author: cns
"""

import random, os,subprocess

contFile = 'nls_control.d'
compFile = 'compile.sh'
exFile = 'nls.bash'
Nruns = 500
base_zeta = 1E-16 
zeta_mod = 10
base_OPR = 0.003
OPR_mod = 1000
nH2 = 0.499975

random.seed(716381)

os.system('rm -rf model_run*')

for i in range(0,Nruns):
    #Mkdir with os package
    temp_path = 'model_run_'+str(i)
    os.mkdir(temp_path)
    
    #Copy files into new directory
    cmd = 'cp * ./' + temp_path + '/'
    os.system(cmd)

    #Generate pseudo-random numbers
    while True:
        r1 = random.random()
        r2 = random.random()
        if r1 != 0.0 and r2 != 0.0:
            break
        
    #Calculate new parameter values
    temp_zeta = base_zeta*zeta_mod*r1
    temp_OPR = base_OPR*OPR_mod*r2
    pH2 = nH2/(1+temp_OPR)
    oH2 = temp_OPR*pH2
    line = '{:.4f}  {:.6e}  {:.6e}'.format(temp_OPR,oH2,pH2)
    print line
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
        if i == 30:
            newline = line[:14]+'{:1.3e} '.format(temp_zeta)+line[24:]
            newline = newline[:19] + 'D' + newline[20:]
            outf.write(newline)
        elif i == 73:
            newline = line[:14] + '{:.6e}'.format(oH2) + line[26:]
            newline = newline[:22] + 'D' + newline[23:]
            outf.write(newline)
        elif i == 74:
            newline = line[:14] + '{:.6e}'.format(oH2) + line[26:]
            newline = newline[:22] + 'D' + newline[23:]
            outf.write(newline)
        else:
            outf.write(line)
    outf.close()
    
    #Change into new directory
    os.chdir(temp_path)
    
    #Recompile with os
    print 'Now recompiling'
    cmd = './' + compFile
    subprocess.call(cmd,shell=True)

    #Run with os
    print 'Starting Nautilus'
    cmd = './'  + exFile
    subprocess.call(cmd,shell=True)

    #Change back into home directory
    os.chdir('..')