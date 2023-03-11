import os, shutil, datetime
#import the os and shutil modules to move the files and the datetime module to check the dates

src_dir = "C:\\Users\\User\\Downloads"
#define the source directory

dst_dir = "T:\\archive"
#define the destination directory

for root, dirs, files in os.walk(src_dir):
#loop through all the files and directories in the source directory
    for file in files:
#loop through all the files
        src_file = os.path.join(root, file)
#get the source file path
        mod_time = os.stat(src_file).st_mtime
#get the modification time of the file
        m_time = datetime.datetime.fromtimestamp(mod_time)
#convert the modification time to a datetime object
        if (datetime.datetime.now() - m_time).days > 30:
#check if the file is older than 30 days
            dst_file = os.path.join(dst_dir, file)
#get the destination file path
            shutil.move(src_file, dst_file)
#move the file to the destination directory