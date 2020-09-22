# Write your code here.
import os, sys

n = len(sys.argv)

for x in range(1,n):
    if os.path.exists(sys.argv[x]):
        f = open(sys.argv[x], "r")
        print("contents of " + sys.argv[x],f.read())
    else:
        print("This file doesn't exists! :" + sys.argv[x])
