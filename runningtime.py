#!/usr/local/bin/python

from timeit import Timer
from datetime import datetime
import sys
import commands

t = Timer("""solveIt(getdata("data/ks_30_0"))""", "from solver import solveIt, getdata")

result = t.repeat(1,1)[0]
str = "%.4fs @ %s\n" % (result, str(datetime.now()))

with open("runtimes.txt","a") as f:
    if len(sys.argv) > 1:
        anno = ' '.join(sys.argv[1:]) + "\n"
        dashes = "-"*(len(anno)-1) + "\n" 
        f.write(dashes + anno)
    f.write(str)
    

print commands.getoutput("tail runtimes.txt")
