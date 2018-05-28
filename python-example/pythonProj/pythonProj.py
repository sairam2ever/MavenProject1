#!/usr/bin/python
import sys


# Function definition is here
def printme( str ):
    # This prints a passed string into this function
    print (str)
    return;

# Now you can call printme function
printme('Sample output: %s, %s, %s' % (str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])))
printme("Hello from Python Project");
