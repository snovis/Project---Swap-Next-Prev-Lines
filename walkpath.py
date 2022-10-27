# Test iterating over a file directory

# import required module
from cmath import e
from genericpath import isdir
import os
import glob
from pathlib import Path
 
# assign directory
directory = 'E:\\NovisVault'
 
# iterate over files in
# that directory
print("\n","=" * 80)
print(" Use Path().glob()\n")
files = Path(directory).glob('*.md')
for file in files:
    print(file)


# try the os.scandir method 
# iterate over files in
# that directory
print("\n","=" * 80)
print(" Use Scandir\n")
for filename in os.scandir(directory):
    if filename.is_file():
        print(filename.path)


print("\n","=" * 80)
print(" Use os.walk\n")

# iterate over files in
# that directory
# for root, dirs, files in os.walk(directory):
#     for filename in files:
#         print(os.path.join(root, filename))


        # import required module
 

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



