#first check to see if the file exist or not before deletion
#!/usr/bin/python
import os
myfile="/tmp/foo.txt"
 
## if file exists, delete it ##
if os.path.isfile(myfile):
        os.remove(myfile)
else:    ## Show an error ##
        print("Error: %s file not found" % myfile)