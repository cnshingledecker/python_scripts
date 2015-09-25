# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:52:17 2015

@author: cns
"""

import math,random,os,subprocess

collapse_control = 'ff_collapse_header_mod.f90'
nautHead = 'nls_header_mod.f90'
contFile = 'nls_control.d'
compFile = 'compile.sh'
exFile = 'nls.bash'
Nruns = 10
zeta_min = 1E-18 
zeta_max = 1E-14 
warmUpTemp = 24 #Final warm-up temperature
wut_min = warmUpTemp*100 #I think there is a limit to 1K/100yr
wut_max = 1E6 #an arbitrary upper value



os.system('rm -rf zeta_run*')
os.system('rm -rf temp')
os.system('rm collapse_zeta.out')

results = 'collapse_zeta.out'

random.seed(716381)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

for j in range(0,Nruns):

    #Remove the old physical conditions file
    os.system('rm physical_evolution.d')
    
    #Generate new warm-up time
    r0 = random.random()
    temp_wut = 10**(r0*math.log10(wut_min) + (1-r0)*math.log10(wut_max))
    print '%1.3e' % temp_wut
    writeout = str(temp_wut) + ','
    resf = open(results,'a')
    resf.write(writeout)
    resf.close()
    
    #Edit the collapse header file
    infile = './' + collapse_control 
    i = 0
    inf =  open(infile,'r')
    lines = inf.readlines()
    inf.close()
    outf = open(infile,'w')
    for line in lines:
        i = i + 1
        if i == 34:
#            print line[33:42]
            newline = line[:33] + '%1.3e' % temp_wut + line[42:]
            newline = newline[:38] + 'D' + newline[39:]
            newline = newline[:42] + '*YEAR' + newline[47:]
            outf.write(newline)
#            print newline
        else:
            outf.write(line)
    outf.close()

    #Recompile program
#    print 'Recompiling the collapse program'
    os.system('./collapse_compile.ksh')
    
    #Run the program
#    print 'Now running ff_collapse'
    os.system('./ff_collapse')
    
    #Get the number of lines of new physical conditions file
    pelines = file_len('physical_evolution.d')
    print pelines,'lines in physical_evolution.d'

    
    #Edit the nls_header file with the number of lines in phys_ev.d
#    print 'Starting editing the header file'
    infile = './' + nautHead
    i = 0
    inf =  open(infile,'r')
    lines = inf.readlines()
    inf.close()
    outf = open(infile,'w')
    for line in lines:
        i = i + 1
        if i == 110:
#            print line
#            print line[34:37],'is the value of the header file'
            newline = line[:34] + str(pelines) + line[37:]
            outf.write(newline)
            print newline
        else:
            outf.write(line)
    outf.close()
   
    
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
 
