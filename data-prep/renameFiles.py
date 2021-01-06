# Importing necessary libraries.
import glob
import os
import shutil
directory = '/home/luvitusmaximus/Desktop/Course/ASR/FSDD/recordings/'
dirc = '/home/luvitusmaximus/Desktop/Course/ASR/FSDD/renamed/'
filenames = glob.glob(directory + '*.wav')
speaker = {'theo':'01','lucas':'02','nicolas':'03','jackson':'04','george':'05','yweweler':'06'}
digits = ["%.2d" % i for i in range(0,10)]
number = ["%.2d" % i for i in range(0,50)]
for file in filenames:
    name = file.split(directory)[1]
    name = name.split('.')[0]
    data = name.split('_')[0]
    spk = name.split('_')[1]
    num = name.split('_')[2]
    newname=speaker[spk]+number[int(num)]+digits[int(data)]+'.wav'
    place = dirc + newname 
    shutil.copyfile(file,place)