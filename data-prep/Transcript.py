# Import necessary libraries.
import glob
import shutil
import os
import numpy as np
directory = '/home/luvitusmaximus/kaldi/egs/digits/data/'
filenames = sorted(glob.glob(directory +'*.wav'))
dic = {'00':'zero','01':'one','02':'two','03':'three','04':'four','05':'five','06':'six','07':'seven','08':'eight','09':'nine',}

for file in filenames:
    #print(file)
    name = file.split(directory)[1]
    #print(name)
    nameE = name.split('.')[0]
    #print(nameE) # Utterence ID
    spk = nameE[0:2]
    #print(spk) # Speaker ID
    data = nameE[4:6]
    #print(data)
    #print(dic[data])
    print(nameE,'\t',dic[data])
