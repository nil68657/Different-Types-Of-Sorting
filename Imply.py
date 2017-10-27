import numpy as np
import pandas as pd

from collections import defaultdict

data = pd.read_csv('F:\Imply\daccess.log', header = None)

print(data)

#adict = {}

d = defaultdict(list)

for index, row in data.iterrows():

 key = row[1]

 d[key].append(row[2])

#print(d)

d1 = defaultdict(list)

d2 = defaultdict(list)
for key,value in d.items():

 count = len(value)

 d1[key].append(count)

 d2[count].append(key)

#print(d2)

#print(d2)

input = input()

for key,value in d2.items():

 if(key == input):
   #print(d2[key])
    s = d2[key]
   #print(d2[key])
    print(d2[key])
    f = open('out.txt', 'w')
    print >> f, 'Fetching user-ids for at-least N distinct paths:\n', str(d2[key]).replace("[","").replace("]", "").replace("L", "").replace(",", "\n").replace(" ","") 
    print(str(d2[key]).replace("[","").replace("]", "").replace("L", "").replace(",", "\n"))