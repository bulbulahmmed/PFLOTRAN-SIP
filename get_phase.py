#!Pythoni
import numpy as np
import pandas as pd
import time

#=========================;
#  Start processing time  ;
#=========================;
tic = time.clock()

#=================================================================================;
#  Function no-1: Read complex potential file, split into real and imag part      ;
#  combine the real and imag part to make it complex number and finally make it   ;
#  convert it to phase using np.angle([array])                                    ;
#=================================================================================;

def get_phase(potentialfile):
    #
    pot_data       = np.genfromtxt(potentialfile, delimiter='', skip_header=1, skip_footer=0)        #Sig data
    real_part      = pot_data[:,0]
    imag_part      = pot_data[:,1]
    
    complex_pot    = real_part + 1j*imag_part
    phase          = np.angle(complex_pot)
    return phase


#=========================================;
#  Function no-2: Find potential number   ;
#=========================================;
def get_potential_number(potentialfile):
    f1 = open(potentialfile, 'r')
    str = f1.readline().split()
    npotential = int(str[0])
    return npotential


#====================================;
#  Function-4: Create phase    file  ;
#====================================;
def write_phase_file(phase, npotential, phase_file):

    with open(phase_file, 'w') as fout:
        fout.write(     str(npotential) + '          ' +str(1) + '\n')
        np.savetxt(   fout, phase, fmt='%8.6e', delimiter = '\t')
 

#************************************************************;
# Input parameter set up and run function                    ;
#************************************************************;
pot_list  = range(1,13) #Potential file number list

for i in pot_list: #Iterate over the potential no. list

    #--------------------------------------------------------;
    #  Create potential file and phase file strings to read  ;
    #--------------------------------------------------------;
    potentialfile = 'potential.'
    phase_file    = 'phase.'
    potentialfile = potentialfile + str(i)
    phase_file    = phase_file + str(i)
    print potentialfile, phase_file

    #--------------------------------------------------------;
    #  Create potential file and phase file strings to read  ;
    #--------------------------------------------------------;
    phase         = get_phase(potentialfile) #Get the phase from real and complex potential
    npotential    = get_potential_number(potentialfile) # Get number of potential data
    write_phase_file(phase, npotential, phase_file) #Write phase

#======================;
# End processing time  ;
#======================;
toc = time.clock()
print 'Time elapsed in seconds = ', toc - tic


