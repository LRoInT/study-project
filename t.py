import getopt
import sys
a,b=getopt.getopt(sys.argv[1:], "d:h", ["download="])
print(a)
print(b)
