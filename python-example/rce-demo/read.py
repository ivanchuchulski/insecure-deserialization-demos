#!/usr/bin/python3
import pickle
import sys

filename=sys.argv[1]

print(filename)

with open(filename, 'rb') as data_file:
  mydata = pickle.load(data_file)
  print("read object from object.ser:")
  print(mydata)
