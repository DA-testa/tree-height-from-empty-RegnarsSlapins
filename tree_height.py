# python3

import sys
import threading
import numpy as np

def compute_height(inputArray):
    height=0
    level = np.where(inputArray==-1)[0]
    while len(level)!=0:
        height=height+1
        nextlevel=np.array([]).astype(int)
        for i in range(len(level)):
            sublevel=np.where(inputArray==level[i])
            nextlevel=np.concatenate((nextlevel,sublevel),axis=None)
        level=nextlevel
    return height
line = "---------------------------------------"
def main():
    # implement input form keyboard and from files
    
    entry=input()
    if entry[0]=="F":
        filename=input()
        file=open(filename, "r")
        file.readline() # Skips n (idk what I need it for)
        values = list(map(int, file.readline().split()))
        values = np.array(values)
    else:
        count=input() # Skips n (idk what I need it for)
        values=input()
        values = list(map(int, values.split()))
        values = np.array(values)
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
