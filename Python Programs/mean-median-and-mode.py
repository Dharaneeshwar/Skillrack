﻿Mean, Median, and Mode
Given an array, X, of N  integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one. 
Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3, 7.0  format).
Input Format
The first line contains an integer, N, denoting the number of elements in the array. 
The second line contains N space-separated integers describing the array's elements.
Constraints
· 10 <= N <= 2500
· 0 < Xi <= 10^5, where Xi is the ith  element of the array.
Output Format
Print 3 lines of output in the following order:
1. Print the mean on a new line, to a scale of 1 decimal place (i.e., 12.3, 7.0).
2. Print the median on a new line, to a scale of  1 decimal place (i.e., 12.3, 7.0).
3. Print the mode on a new line; if more than one such value exists, print the numerically smallest one.
Sample Input
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
Sample Output
43900.6
44627.5
4978
Explanation
Mean:
We sum all  elements in the array, divide the sum by , and print our result on a new line.
Median:
To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order. The sorted array . We then average the two middle elements:and print our result on a new line.
Mode:
We can find the number of occurrences of all the elements in the array:
 4978 : 1
11735 : 1
14216 : 1
14470 : 1
38120 : 1
51135 : 1
64630 : 1
67060 : 1
73429 : 1
99233 : 1
Every number occurs once, making 1 the maximum number of occurrences for any number in X. Because we have multiple values to choose from, we want to select the smallest one, 4978, and print it on a new line.
from statistics import mean
import collections
import math
n,l1=int(input()),[]
l=sorted([int(i)for i in input().split()])
print("%.1f"%mean(l))
print((l[(n-1)//2]+l[math.ceil((n-1)/2)])/2)
a=collections.Counter(l)
x=list(a.keys())
y=list(a.values())
for i in range(len(y)):
    if y[i]==max(a.values()):
        l1.append(x[i])
if min(a.values())==max(a.values()):
    print(min(l))
else:
    print(min(l1))
