#%%
import numpy as np
import os.path as path
from io import StringIO


# option = 'Temperature'
#filename = 'Power_ON_5C.txt'
#filename = 'Power_ON_6C.txt'
#filename = 'Power_ON_7C.txt'
# filename = 'Power_ON_18C.txt'

#option = 'Mode'
#filename = 'Cooling.txt'
#filename = 'Heating.txt'
#filename = 'Fan.txt'

#option = 'Wind'
#filename = 'Low.txt'
#filename = 'Mid.txt'
#filename = 'High.txt'
#filename = 'Turbo.txt'
#filename = 'Auto.txt'

# option = 'Timer'
# filename = '5h.txt'

option = 'Blade'
filename = 'Fixed.txt'

with open(path.join('Sample', option, filename)) as f:
    contents = f.read()
    while contents[-1] == ',' or contents[-1] == ' ' or contents[-1] == '\n':
        contents = contents[:-1]
    str_io = StringIO(contents.split(')')[1])
    timings = np.loadtxt(str_io, delimiter=',')[:-1]

timings = timings.reshape(-1,2)

bins = []
binary = ''


for i, timing in enumerate(timings):
    if timing[0] > 4000:
        pass
    elif timing[1] < -4000:
        bins.append(''.join(reversed(binary)))
        binary = ''
    else:
        if timing[1] < -1200:
            binary += '1'
        else:
            binary += '0'
        
        if i == len(timings) -1:
            bins.append(''.join(reversed(binary)))

if bins[0] == bins[1]:
    print(hex(int(bins[0],2)))
else:
    print('IR Signal Broken')


# %%
