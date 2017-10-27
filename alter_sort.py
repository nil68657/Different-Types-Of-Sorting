#Created on Thu Oct 12 20:05:28 2017

# @author: nilan

from itertools import permutations

x = raw_input() #Range of n till which we want to sort
x=int(x)        #Conversion of string to integer
total_list = []
reqd_list = []

def alternating_sort(x):
    
    total_list = list(permutations(range(1, x + 1)))
    
    for l in total_list:
    
            for i in range(1, x, 2):
                if i != (x-1):
                    if (l[i] > l[i - 1]) and (l[i] > l[i + 1]):
                        count = 0
                        count += 1
                    elif i == (x-1):
                      if l[i] > l[i - 1]:
                       count += 1
                      if count == (x/2):
                           reqd_list.append(l)
                           count = 0
                           return
    
alternating_sort(x)

print(reqd_list)

print "Total number of possible combinations of alternating sorts: ", len(reqd_list)