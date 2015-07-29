# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:10:12 2015

@author: cns
"""
source    = 'W51C' #name of the astronomical source 
warm_time = 1E5    #time at which warm-up begins
max_time  = 1.5E7    #max simulation time
n_outs    = 10     #outputs per decade
t_init    = 10     #initial temperature in K
t_final   = 24     #final temperature in K
warm_type = 0      #0=step function, 1=exponential
density   = 1E4    #density in 1/cm3
Av        = 10     #visual extinction


#Form output filename and open
basename  = '_physical_conditions.d'
filename  = source + basename
outf = open(filename, 'w')

#Calculate the number of output times
decades = len(str(max_time))-3
n_points = (decades)*n_outs
print 'the number of decades is',decades


#Initialize arrays
time_arr = []
density_arr = []
av_arr = []
temp_arr = []

#Calculate initial time-step
time=0
exponent = 0
t_step=10**exponent
print 't_step is',t_step

#Initialize temperature
temp = t_init

counter = 0
i = 0
while True:
    density_arr.append(density)
    av_arr.append(Av)
    time_arr.append(time)
    if warm_type == 0:
        if time >= warm_time:
            temp = t_final
    temp_arr.append(temp)
    if counter == n_outs+1:
        print 'counter =',counter,' and exponent =',exponent
        if exponent != decades:
            if exponent == decades-1 and counter == 10:
                print 'HERE WE GO'
                t_step = (max_time-10**decades)/10
                print 't_step is',t_step
            exponent = exponent + 1
            if exponent != decades:
                t_step = 10**exponent
        counter = 0
    counter = counter + 1
    time = time+t_step
    newline = ('  {:1.6e}  {:1.6e}  {:1.6e}  {:1.6e}\n'.format(time_arr[i],density_arr[i],av_arr[i],temp_arr[i]))
    outf.write(newline)
    i = i + 1
    if time >= max_time:
        break

print 'i =',i
print 'Ending script'
outf.close()