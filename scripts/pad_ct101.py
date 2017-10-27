
import os
from os import listdir
from os.path import isfile, join
import subprocess
import re
import numpy as np

WIDTH=224
HEIGHT=224

mypath='padded_101'
dirs = [f for f in listdir(mypath) if f != 'BACKGROUND_Google']

for dir in dirs:
    onlyfiles = [f for f in listdir(mypath+'/'+dir) if isfile(join(mypath+'/'+dir, f))]
    for f in onlyfiles:
        output = subprocess.check_output(['identify', '{}'.format(mypath+'/'+dir+'/'+f)])
        dims = map(lambda x: int(x), output.split(' ')[2].split('x'))
        dW = dims[0]-WIDTH
        dH = dims[1]-HEIGHT

        osW = dW/2
        osH = dH/2

        print 'Dims: {}'.format(dims)
        if dW != 0 or dH != 0:
            cmd = 'convert {} -resize {}x{}  -gravity center -background "rgb(255,255,255)" -extent {}x{} {}'.format(mypath+'/'+dir+'/'+f, WIDTH, HEIGHT, WIDTH, HEIGHT, mypath+'/'+dir+'/'+f)
            print cmd
            os.system(cmd)
            #os.system('identify {}'.format(mypath+'/'+dir+'/'+f))

