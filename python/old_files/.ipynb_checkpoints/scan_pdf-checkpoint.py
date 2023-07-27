import os
import os.path
import re

def print_py ():
    for (root,dirs,files) in os.walk('.', topdown=0):
        for name in files:
            path = os.path.join(root,name)
            #print(os.path.join(root,name))
            #filtering conditions and exiting current iteration if conditions are met
            if not re.search (r".*\.py", path): continue
            if re.search(r" ",path): continue
            print (path)         
        
            
def cycle ():
    for (root,dirs,files) in os.walk('.', topdown=0):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')
            
print_py()

