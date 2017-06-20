# Thanks to https://stackoverflow.com/questions/17646680/writing-back-into-the-
# same-file-after-reading-from-the-file for the helmp
# There's also a combination of REGEX here to take care of some abnomalities


import tempfile
import sys
import re

#Create temporary file read/write
t = tempfile.NamedTemporaryFile(mode="r+")

#Open input file read-only
i = open('track_00000001.txt', 'r')

#Copy input file to temporary file, modifying as we go
for line in i:
    line = re.sub('[a-zA-Z]+', " ", line)
    t.write(line)

i.close() #Close input file

t.seek(0) #Rewind temporary file to beginning

o = open('track_00000001.txt', "w")  #Reopen input file writable

#Overwriting original file with temporary file contents
for line in t:
   o.write(line)

t.close() #Close temporary file, will cause it to be deleted
