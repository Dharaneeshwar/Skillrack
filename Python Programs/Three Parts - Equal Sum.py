"""
Three Parts - Equal Sum
The program must accept an integer array of size N as the input. The program must print YES if it is possible to split the array into three parts with equal sum. Else the program must print NO as the output.

Boundary Condition(s):
3 <= N <= 100
-1000 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:
8
0 8 -6 5 -3 4 1 -3

Output:
YES

Explanation:
The given 8 integers are 0, 8, -6, 5, -3, 4, 1 and -3.
The sum of the first three integers is 2 (0 + 8 + (-6)).
The sum of the next two integers is 2 (5 + (-3)).
The sum of the last three integers is 2 (4 + 1 + (-3)).
So YES is printed as the output.

Example Input/Output 2:
Input:
7
0 -5 -4 5 -2 7 -7

Output:
NO

"""