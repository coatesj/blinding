#!/usr/bin/env python

import glob, os, shutil, datetime, getpass

from random import shuffle

import tkinter, tkinter.filedialog



root = tkinter.Tk()

dirname = tkinter.filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

if len(dirname) > 0:

    print ("You chose %s" % dirname) 


files = glob.glob("%s/*"%dirname)

if len(files) > 0:

    print ("Which contains %s files" % len(files)) 


n_file = list(range(1, len(files)+1))

shuffle(n_file)

# new directory for blinded files

blind_dir = "%s_blinded"%dirname

os.mkdir(blind_dir)

print ("New directory for blinded files is %s"%blind_dir)

# open write file for blinded list

now = datetime.datetime.now()

blind_list = open("%s/blinded_file_list.txt"%blind_dir, 'w')

blind_list.write("Files blinded by %s at %d:%d on date %d %d %d\n"%(getpass.getuser(), now.hour, now.minute, now.year, now.month, now.day))

blind_list.write("blinded file\toriginal file\n")

# loop 

print ("Blinding files...")

for i in list(range(len(files))):

    print ("%s / %s"%(i+1, len(files)))

    # new blinded file name

    b_fnm = "%s/%s.%s"%(blind_dir,n_file[i],files[i].split('.')[-1])

    # write into blinded list

    blind_list.write("%s\t%s\n"%(b_fnm,files[i]))

    # copy file to blinded directory, with blinded file name

    shutil.copyfile(files[i], b_fnm)

    
blind_list.close()

print ("Finished.")
