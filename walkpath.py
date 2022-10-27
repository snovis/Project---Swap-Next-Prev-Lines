# Test iterating over a file directory

# import required module
from cmath import e
from genericpath import isdir
import os
import glob
from pathlib import Path
 
# assign directory
directory = 'E:\\NovisVault'
 

print("\n","=" * 80)
print(" Use glob.iglob\n")

# iterate over files in
# that directory
files = []
for filename in glob.iglob(f'{directory}/*'):
    if os.path.isfile(filename):
        files.append(filename)
    else:
        if os.path.isdir:
            print(".",end="")
        files.append("["+filename+"]")

print("\nResults")

files.sort();
for f in files:
    print(f)



