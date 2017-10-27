#Created on Wed Oct 18 22:09:05 2017

# @author: nilan

from itertools import permutations

reqd_list = []
x=raw_input()   #Range of n till which we want to sort
x=int(x)        #Conversion of string to integer

def double_sort(x):

    total_list = list(permutations(range(1, x + 1)))

    if (x % 4) == 1:  # Sorting possibility for x= 5,9,....
        count = 0

        for l in total_list:
            for i in range(2, x + 1, 4):
                if (l[i] > l[i - 1]) and (l[i - 1] > l[i - 2]) and (l[i] > l[i + 1]) and (l[i + 1] > l[i + 2]):
                    count += 1

            if count == len(range(2, x + 1, 4)):
                reqd_list.append(l)
            count = 0

        print(reqd_list)
        print "Total number of double alternating sorts: ", len(reqd_list)

    elif (x % 4) == 2:  # Sorting possibility for x=6,10,....
        count = 0

        if x == 2:
            print "There is only 1 possible double alternating sort"
            return

        for l in total_list:
            for i in range(2, x, 4):
                if (l[i] > l[i - 1]) and (l[i - 1] > l[i - 2]) and (l[i] > l[i + 1]) and (l[i + 1] > l[i + 2]) and (l[i + 2] < l[i + 3]):
                    count += 1

            if count == len(range(2, x, 4)):
                reqd_list.append(l)
            count = 0

        print(reqd_list)
        print "Total number of double alternating sorts: ", len(reqd_list)

    elif (x % 4) == 3:  # Sorting possibility for x=7,11,....
        count = 0
        iterations = list(range(2, x + 1, 4))

        for l in total_list:
            for i in iterations:
                if iterations[-1] == i:  # Only for the last element
                    if (l[i] > l[i - 1]) and (l[i - 1] > l[i - 2]):
                        count += 1
                elif (l[i] > l[i - 1]) and (l[i - 1] > l[i - 2]) and (l[i] > l[i + 1]) and (l[i + 1] > l[i + 2]):
                    count += 1

            if count == len(range(2, x + 1, 4)):
                reqd_list.append(l)
            count = 0

        print(reqd_list)
        print "Total number of double alternating sorts: ", len(reqd_list)

    elif (x % 4) == 0:  # Sorting possibility for x=4,8,12,..
        count = 0
        iterations = list(range(2, x, 4))

        for l in total_list:
            for i in iterations:
                if iterations[-1] == i:  # Last element
                    if (l[i] > l[i - 1]) and (l[i - 1] > l[i - 2]) and (l[i] > l[i + 1]):
                        count += 1
                elif (l[i] > l[i - 1]) and (l[i - 1] > l[i - 2]) and (l[i] > l[i + 1]) and (l[i + 1] > l[i + 2]):
                    count += 1

            if count == len(range(2, x, 4)):
                reqd_list.append(l)
            count = 0

   
#print "Total number of possible combinations of double alternating sorts: ", len(reqd_list)
print(reqd_list)
        
double_sort(x) #Invoke function to double sort

