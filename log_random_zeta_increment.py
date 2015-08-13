# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:52:17 2015

@author: cns
"""

import math,random,os,subprocess

contFile = 'nls_control.d'
compFile = 'compile.sh'
exFile = 'nls.bash'
Nruns = 500
zeta_min = 1E-18 
zeta_max = 1E-14 


os.system('rm -rf zeta_run*')
os.system('rm -rf temp')
os.system('rm zeta.out')

results = 'zeta.out'

random.seed(716381)

for j in range(0,Nruns):
    #Mkdir with os package
    temp_path = 'temp'
    os.system('rm -rf temp')
    os.mkdir(temp_path)
    
    #Copy files into new directory
    cmd = 'cp * ./' + temp_path + '/'
    os.system(cmd)
        
    #Calculate new parameter values
    r1 = random.random()
    temp_zeta = 10**(r1*math.log10(zeta_min) + (1-r1)*math.log10(zeta_max)) 
    temp_res =  str(temp_zeta)  + '\n'
    resf = open(results,'a')
    resf.write(temp_res)
    resf.close()

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
            newline = line[:14] + '%1.3e' % temp_zeta + line[24:]
            newline = newline[:19] + 'D' + newline[20:]
            outf.write(newline)
            print newline
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
    newdir = 'zeta_run_'+str(j)
    os.mkdir(newdir)
    cmd = 'cp ./temp/output_1D* ./' + newdir + '/'
    os.system(cmd)
    cmd =  'cp ./temp/rates1D.* ./' + newdir + '/'  
    os.system(cmd)
    cmd = 'rm -rf temp/'
    os.system(cmd)
 
