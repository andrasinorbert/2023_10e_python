import sys

filename=sys.argv[1]

file=open(filename)
sorok=file.readlines()
file.close()

print(sorok)