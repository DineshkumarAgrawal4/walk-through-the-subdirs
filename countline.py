import subprocess
import os
import sys
#This is a very simple program to count the line of some files with suffix
def countlines(directory,suffix):
    print('lines'+' '+'dir')
    for (thisdir,subsdir,thisfile) in os.walk(directory):
        for file in thisfile:
            if file.endswith(suffix):
                file=os.path.join(thisdir,file)
                subprocess.call(['wc','-l',file])
                
if __name__=='__main__':
    directory=sys.argv[1]
    suffix=sys.argv[2]
    countlines(directory,suffix)
