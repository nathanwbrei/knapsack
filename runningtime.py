

from timeit import Timer
from datetime import datetime

t = Timer("""solveIt(getdata("data/ks_30_0"))""", "from solver import solveIt, getdata")

result = t.repeat(1,1)[0]

with open("runtimes.txt","a") as f:
    f.write("Got %.4fs @ %s\n" % (result, str(datetime.now())))

