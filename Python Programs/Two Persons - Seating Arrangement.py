"""
Two Persons - Seating Arrangement
There are N chairs arranged in two columns in a room. Each column has exactly N/2 chairs (where N is always even). The chairs are numbered from 1 to N as given below.
1 2
3 4
5 6
7 8
9 10
and so on.
There are K persons who have already occupied their chairs in the room. The program must accept K integers representing the chairs occupied by the K persons and the value of N as the input. The program must print the number of ways two new persons can sit next to each other (i.e., one person on the left and the other on the right, or one person is directly above or below the other person).

Boundary Condition(s):
1 <= K <= N <= 1000
1 <= Each integer value <= N

Input Format:
The first line contains K.
The second line contains K integers separated by a space.
The third line contains N.

Output Format:
The first line contains the number of ways two new persons can sit next to each other.

Example Input/Output 1:
Input:
4
1 5 6 11
12

Output:
7

Explanation:
The 12 chairs can be arranged as given below.
# 2
3 4
# #
7 8
9 10
# 12
The hash symbols (#) represent the occupied chairs.
There are 7 ways to seat two new persons next to each other.
(2, 4), (3, 4), (7, 8), (7, 9), (8, 10), (9, 10) and (10, 12).
So 7 is printed as the output.

Example Input/Output 2:
Input:
5
8 3 10 16 7
16

Output:
10

"""
Python Code:

Num=int(input())
Array=list(map(int,input().split()))
Temp=int(input())
Array=set(Array)
counter=0
for index in range(1,Temp):
    if index not in Array:
        if index+2<=Temp and index+2 not in Array:
            counter+=1 
        if index&1 and index+1 not in Array:
            counter+=1
print(counter)


/* C Code by Abi Karthcik */

#include <iostream> 
#include<map>
using namespace std;

int main()
{
    map<int,bool> a;
    int n,b,x,s=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&b);
        a[b]=1;
    }
    scanf("%d",&x);
    for(int i=0;i<x;i+=2){
        s+=(!(a[i+1]||a[i])+!(a[i+2]||a[i])+!(a[i+3]||a[i+1]));
    }
    printf("%d",s);
}
