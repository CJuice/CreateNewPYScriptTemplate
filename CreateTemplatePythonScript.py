###################################
# Script:  tester.py
# Author:  
# Date:  06/11/2015
# Purpose:  This script creates a brand new python script file with a user tailored header.
# Inputs:  path_root; filename; author; purpose; inputs; outputs
# Outputs:  The output is a python script file in the location of choice with the file name of choice.
###################################
import sys
#
#
#
# Start Scripting Below

#store the root path as a string
path_root = raw_input("Paste the root path where the new file will be created.")
#print "You pasted " + path_root


#store the file name as a string, second variable adds the .py extension
filename = raw_input("What is the name of the file?")
filename_py = filename + ".py"
#print "You entered: " + filename
#print "The file will be called " + filename_py


#concatenate the root with the file name and .py, use for check exists
fullpath = path_root + "\\" + filename_py
#print fullpath

#concatenate the root with the file name and .py, along with r - I thought this was necessary but isn't working!
#fullpath_r = "r" + "\"" + path_root + "\\" + filename_py + "\""
#print fullpath_r

#check to see if it exists
import os.path
if os.path.isfile(fullpath) == True:
    print "*****\nThe file " + fullpath + "  already exists. Please start this process over.\nEnding Script!\n*****"
    sys.exit()
#else:
    #print fullpath + "  has been created."
    
#Create the brand new file using the write option
newdoc = open(fullpath, "w")
#print "File Opened"
newdoc.close()

#Gather the necessary information from the user
author = raw_input("What is your name? ")
            # grab the date, dd/mm/yyyy format
import time
date = (time.strftime("%m/%d/%Y"))
purpose = raw_input("What is the purpose of the script?  ")
inputs = raw_input("What are the inputs?  ")
outputs = raw_input("What are the outputs?  ")

#print date
#print purpose
#print inputs
#print outputs

#now to open the file and write the header information
newdoc = open(fullpath, "r+")
newdoc.write("#"*35)
newdoc.write("\n# Script:  " + filename_py)
newdoc.write("\n# Author:  " + author)
newdoc.write("\n# Date Created:  " + date)
newdoc.write("\n# Purpose:  " + purpose)
newdoc.write("\n# Inputs:  " + inputs)
newdoc.write("\n# Outputs:  " + outputs)
newdoc.write("\n# Modifications:  \n")
newdoc.write("#"*35)
newdoc.write("\nimport sys, arcpy\n" + "#\n"*3 + "# Start Scripting Below")

newdoc.close()
print "Your " + filename_py + " file has been created."
