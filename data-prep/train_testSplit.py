# Import necessary libraries.
import os
import glob
import shutil
directory = '/home/luvitusmaximus/Desktop/Course/ASR/FSDD/renamed/'
home = '/home/luvitusmaximus/Desktop/Course/ASR/FSDD/'
filenames = (glob.glob(directory + '*.wav'))

for file in filenames:
    print(file)
    name = file.split(directory)[1]
    print(name)
    nameE = name.split('.')[0]
    print(nameE)
    spk = nameE[0:2]
    print(spk)
    if spk == '01':
        place = home + 'test/' + name
        shutil.copyfile(file,place)
    else:
        place = home + 'train/' + spk + '/'+ name
        shutil.copyfile(file,place)