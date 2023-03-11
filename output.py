.

import os #imports os library
import shutil #imports shutil library
import time #imports time library

#sets the current working directory
src_dir = 'C://Users//Downloads' 

#sets the destination directory
dst_dir = 'T://archive'

#gets the current time
now = time.time()

#loops through all the files in the source directory
for file in os