import sys
import glob
import os
# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames
glo = glob.glob(hdir)
print(glo)
# TODO: use os.path.getsize to find each file's size
files = os.listdir()
for file in files:
    size = os.path.getsize(file)
    print(files, size)
# TODO: Add a test to only display files that do not have a size of zero
files = os.listdir()
for file in files:
    size = os.path.getsize(file)
    if size >0:
        print(files, size)
# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
files = os.listdir()
for file in files:
    size = os.path.getsize(file)
    path = os.path.basename(file)
    print(path)