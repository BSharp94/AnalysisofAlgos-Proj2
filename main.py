import numpy as np
import time
import random
import math
import matplotlib.pyplot as plt
#Files to read from
F1 = "file1.txt"
F2 = "file2.txt"

def get_substring_list(file_string):
    substring_list = []
    for offset in range(len(file_string)):
        for str_length in range(1,len(file_string)-offset+1):
            #all possible substrings of
            substring = file_string[offset:(offset+str_length)]
            substring_list.append(substring)

    return substring_list

def compare_lists(list1,list2):
    largest_substring = ""
    largest_substring_size = 0

    for item1 in list1:
        str_size = len(item1)
        if str_size < largest_substring_size:
            continue
        for item2 in list2:
            if item1 == item2 and str_size > largest_substring_size:
                #record largest
                largest_substring = item1
                largest_substring_size = len(item1)

    return largest_substring

def run(size):
    string1,string2 = "",""
    for i in range(size):
            string1 = string1 + str(random.randint(1,10))
    for i in range(size):
            string2 = string2 + str(random.randint(1,10))

    start =  time.time()
    str1_list = get_substring_list(string1)
    str2_list = get_substring_list(string2)
    largest_substring = compare_lists(str1_list,str2_list)
    end =  time.time()
    return (end-start)




if __name__ == '__main__':
    # read files
    file1 = open(F1).read()
    file2 = open(F2).read()

    # print the contents
    print "\n---- File Contents ----"
    print "File 1:",file1,
    print "File 1 length: ",len(file1)
    print "File 2:",file2,
    print "File 2 length: ",len(file2)

    #make file 1 the larger file
    if len(file1) > len(file2):
        tmp = file1
        file1 = file2
        file2 = file1

    #find the largest string
    start =  time.time()
    str1_list = get_substring_list(file1)
    str2_list = get_substring_list(file2)

    print "\n---- String Lists -----"
    print "str1 list: ",len(str1_list)
    print "str2 list: ",len(str2_list)

    largest_substring = compare_lists(str1_list,str2_list)
    end =  time.time()

    print (end - start)

    print "\nLargest Substring: ",largest_substring
    x = [int(10),int(20),int(30),int(40),int(50),int(50),int(60),int(70),int(80),int(90),int(100)]
    y = []
    for xval in x:
        y.append(run(xval))

    plt.plot(x,y)
    plt.title("Run Time vs String Size")
    plt.xlabel("String size")
    plt.ylabel("Run Time (seconds)")
    plt.show()
