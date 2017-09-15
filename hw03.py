# Terry Guan and Naotaka Kinoshita
# soft_dev1 pd7
# HW03 -- StI/O: Divine your Destiny!
# 2017-09-14

import random

#A list with total % * 10 entries, each occupation has its percentage * 10 entries
occupations10 = []

occupations = []

#function to load the information from the file
def load_file(filename):
    with open (filename, 'r') as f:
        fstr = f.read()
        list_split = fstr.split('\n')
        #print list_split
        heading = list_split[0]
        list_split = list_split[1:len(list_split) - 1]
        temp = []
        for item in list_split:
            if item[0] == '"':
                temp2 = []
                temp2.append(item[1:item.index('"', 1)])
                temp2.append(float(item[item.index('",', 1) + 2 :]))
                temp.append(temp2)
            else:
                temp.append(item.split(","))
                temp[len(temp) - 1][1] = float(temp[len(temp) - 1][1])
        occupations = temp[:len(temp) - 2]
        #print occupations
                
def load_occupations():
    for item in occupations:
        for i in range(item[1] * 10):
            occupations10.append(item[0])
    print occupations10
#
def get_random():
    return occupations[random.randint(0,len(occupations) - 1)]

load_file("occupations.csv")

#print (get_random)
