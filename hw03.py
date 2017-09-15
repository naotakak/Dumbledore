# Terry Guan and Naotaka Kinoshita
# soft_dev1 pd7
# HW03 -- StI/O: Divine your Destiny!
# 2017-09-14

import random

#A list with total % * 10 entries, each occupation has its percentage * 10 entries
occupations = []

#text of the .csv file
file_read = ""

#function to load the information from the file
def load_file(filename):
    #    file_open = open(filename)
    #   file_read = file_open.read()
    #  add_entries()
    with open (filename, 'r') as f:
        fstr = f.read()
        list_split = fstr.split('\n')
        heading = list_split[0]
        list_split = list_split[1:len(list_split) - 1]
        list_split = [item.split(',') for item in list_split]
  print list_split
    
#
def get_random():
    return occupations[random.randint(0,len(occupations) - 1)]

load_file("occupations.csv")

#print (get_random)
