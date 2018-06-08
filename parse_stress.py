"""
This script takes the output of 3DEC for stress and converts it into something readable by matlab
"""

import glob
import numpy as np

def parse_stress(paths):
#path = 'C:/Users/Rebecca Napolitano/Documents/datafiles/Romanbondingcourses/2017_11_15_lowfric_persistent/nobc/'
    
    for path in paths:
        
        stress_files = glob.glob(path + '*_stress.dat')
        
        filenames = [f.replace('_stress.dat', '') for f in stress_files]
        
        for filename in filenames:
            fid = open(filename+'_stress.dat', 'r+') #open stress file from 3dec
            txt = fid.read()
            fid.close()
            txt = txt.replace(';','') #remove extra characters
            dat = np.fromstring(txt,sep=' \n')[:-1] # ask numpy to convert string to array
            all_dat = np.reshape(dat[:],(-1,3)) # reshape array from 1D to 2D #-1 means "dont care how long it is, just make 3 columns"
            np.savetxt(filename+'_stress_py.dat', all_dat)