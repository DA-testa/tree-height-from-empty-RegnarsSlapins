# python3

# TODO:
# 1) Implement numpy
# 2) Utilise value count
# 3) Optimize search

import sys
import threading
import numpy as np

test1 = [-1, 0, 4, 0, 3]
test2 = [4, -1, 4, 1, 1]
def compute_height(inputArray):
    max_height=0
    for i in range(len(inputArray)):
        element = inputArray[i]
        height=1
        while element!=-1:
            element=inputArray[element]
            height=height+1
            #print(element)
        if height>max_height:
            max_height=height
    return max_height

line = "---------------------------------------"
def main():
    # Local tests
    #
    # print("Tests")
    # print(line)
    # for k in range(1,10):
    #     testname = "0"+str(k)
    #     answer = testname+".a"
    #     file=open("C:/Users/regna/Documents/GitHub/tree-height-from-empty-RegnarsSlapins/test/"+testname, "r")
    #     file.readline()
    #     file2=open("C:/Users/regna/Documents/GitHub/tree-height-from-empty-RegnarsSlapins/test/"+answer,"r")
    #     input = list(map(int, file.readline().split()))
    #     rez = compute_height(input)
    #     ans=file2.readline()
    #     if int(rez) == int(ans):
    #         print("Test "+ str(k) + " passed")
    #         print("Got: "+str(rez))
    #         print("Expected: "+str(ans))
    #     else:
    #         print("Test "+ str(k) + " failed")
    #         print("Got: "+str(rez))
    #         print("Expected: "+str(ans))
    #     print(line)
    # for j in range(10,26):
    #     testname = str(j)
    #     answer = testname+".a"
    #     file=open("C:/Users/regna/Documents/GitHub/tree-height-from-empty-RegnarsSlapins/test/"+testname, "r")
    #     file.readline()
    #     file2=open("C:/Users/regna/Documents/GitHub/tree-height-from-empty-RegnarsSlapins/test/"+answer,"r")
    #     input = list(map(int, file.readline().split()))
    #     rez = compute_height(input)
    #     ans=file2.readline()
    #     if int(rez) == int(ans):
    #         print("Test "+ str(j) + " passed")
    #         print("Got: "+str(rez))
    #         print("Expected: "+str(ans))
    #     else:
    #         print("Test "+ str(j) + " failed")
    #         print("Got: "+str(rez))
    #         print("Expected: "+str(ans))
    #     print(line)

    # implement input form keyboard and from files
    
    entry=input()
    if entry=="F":
        filename=input()
        file=open(filename, "r")
        file.readline() # Skips TODO: Fix
        values = list(map(int, file.readline().split()))
    else:
        count=input() # Skips TODO: Fix
        values=input()
        values = list(map(int, values.split()))
    print(compute_height(values))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
