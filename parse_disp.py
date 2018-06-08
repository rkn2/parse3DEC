"""
This script takes the output of 3DEC for displacement and converts it into something readable by matlab
"""

import glob
import numpy as np
#paths = ['C:/Users/Rebecca Napolitano/Documents/datafiles/zippervaults/eq_disp/', 
#         'C:/Users/Rebecca Napolitano/Documents/datafiles/zippervaults/2018_2_13_eq/']

def parse_disp(paths):
    
    for path in paths:
        disp_files = glob.glob(path + '*_disp.dat')
        
        filenames = [f.replace('_disp.dat', '') for f in disp_files]
        print(len(filenames))
        
        for filename in filenames:
            print(filename)
            fid = open(filename+'_disp.dat', 'r+') #open disp file from 3dec
            txt = fid.read()
            fid.close()
            txt = txt.replace('(','').replace(')','').replace(',',' ').replace('\n 0\n',' ') #remove extra characters
            dat = np.fromstring(txt,sep=' \n')[:-1] # ask numpy to convert string to array
            all_dat = np.reshape(dat[:],(-1,4)) # reshape array from 1D to 2D #-1 means "dont care how long it is, just make 4 columns"
            np.savetxt(filename+'_disp_py.dat', all_dat)
  

  
#parse_disp(paths)