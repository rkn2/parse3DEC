# -*- coding: utf-8 -*-
"""
Spyder Editor

This file takes text files generated by 3DEC and converts
them into a form readable by MATLAB
"""

import glob
import numpy as np

def parse_info_volume(path):
#path = 'C:/Users/Rebecca Napolitano/Google Drive/Documents/Research/itascatrainingetc/geomreadin/testfolder/' #make sure to change

    info_files = glob.glob(path+'*_info.dat')
    vol_files  = glob.glob(path+'*_vol.dat')
    
    
    if len(info_files) != len(vol_files):
        print('warning: not every info and vol file are paired')
        filenames = []
    else:
        filenames = [f.replace('_info.dat','') for f in info_files]
    
    for filename in filenames:
        fid = open(filename+'_info.dat', 'r+') #open the info file
        txt = fid.read() #read the file
        fid.close()
        txt = txt.replace('(',' ').replace(')',' ').replace(',',' ') # remove extra characters
        dat = np.fromstring(txt,sep=' \n')[:-1] # ask numpy to convert string to array
        all_dat = np.reshape(dat[:],(-1,7)) # reshape array from 1D to 2D #-1 means "dont care how long it is, just make 7 columns"
        fid = open(filename+'_vol.dat', 'r+') #open the vol file
        txt = fid.read() #read the file
        fid.close()
        txt = txt.replace('(',' ').replace(')',' ').replace(',',' ') # remove extra characters
        dat = np.fromstring(txt,sep=' \n')[:-1] # ask numpy to convert string to array
        dat = np.reshape(dat[:],(-1,1))
        all_dat = np.hstack((all_dat,dat)) #hstack is for another column, v stack is for another row
        np.savetxt(filename+'_py.dat',all_dat)