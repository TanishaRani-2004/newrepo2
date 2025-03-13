import sys
def printN(name):
    print(name)
if len(sys.argv)>1:
    print(sys.argv[1])
else:
    printN("Tan")
