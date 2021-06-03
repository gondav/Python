# The program identifies a person based on their DNA, per the below.

import sys
import csv
import re

# open csv and txt files provided in the command line arguments
fcsv = csv.reader(open(sys.argv[1]))
ftxt = open(sys.argv[2])
rtxt = ftxt.read()

# extract the first row from the csv file
for row in fcsv:
    break

# extract the necessary "RTSs" from the csv file
lst = row[1:]

# count the max "RTSs" repeated consecutively in the txt file
RTSmaxlst = list()  # create a list of max RTSs repeated consecutively extracted from the txt file
for RTS in lst:
    pattern = "((?:" + RTS + ")*)"
    RTSmax = len(max(re.findall(pattern, rtxt), key = len)) / len(RTS)
    RTSmaxlst.append(str(int(RTSmax)))

match = False
for row in fcsv:
    name = row[0]
    if row[1:] == RTSmaxlst:
        match = True
        print(name)

if match is False: print("No match")
