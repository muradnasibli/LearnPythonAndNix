# Write your code here.
import os, sys

#Lenght of arguments
n = len(sys.argv)

for x in range(1,n):
    if os.path.exists(sys.argv[x]):
       with open(sys.argv[x]) as f:
           print("Content of :" + sys.argv[x] + "\n", f.read())
    else:
        print("This file doesn't exists! :" + sys.argv[x])
