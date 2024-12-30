#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:43:53 2024

@author: Ben F.

Appends date modified to file names
"""

from os import listdir
from os import path
from os import rename
from datetime import datetime


def append_date_modified_to_filenames(folder_name):
    filenames = listdir(folder_name)
    print(filenames[0:10])
    
    new_filenames = {}
    for i,name in enumerate(filenames):
        date_modified = path.getmtime(folder_name+name) - 25200
        date_modified = datetime.utcfromtimestamp(date_modified).strftime('%Y-%m-%d %H:%M:%S')
        
        split_name = filenames[i].split(".")
        name = ""
        for j in range(len(split_name) - 1):
            name=name+split_name[j]
        extension = split_name[-1]

        new_filenames[name+"."+extension] = str(date_modified) + " - " + name + "." + extension
    
    print("")
    print("")
    
    for old in new_filenames.keys():
        new = new_filenames[old]

        
        try:
            rename(folder_name+old, folder_name+new)
        except:
            print("FAIL")
            print(old)
            print(new)
            print("")
            
        
        
    

