﻿Flip Count - Matrix
The program must accept a matrix of size NxN as the input. The matrix contains only 0's and 1's. The program must transpose the matrix then the program must print the flip count required to make the transpose matrix and original matrix equal. 
Boundary condition(s): 1 <= N <= 50 
Input Format: 
The first line contains the integer value of N. 
The next N lines contain N integers separated by space(s). 
Output Format: The first line contains the flip count required to make the original matrix and the transposed matrix equal. 
Example Input/Output 1: 
Input: 
3 
0 0 1 
1 1 1 
1 0 0 
Output: 
4 
Explanation: 
Orginal matrix 
0 0 1 
1 1 1 
1 0 0 
Transpose matrix 
0 1 1 
0 1 0 
1 1 0 
The number of flips required is 4. Hence the output is 4 
Example Input/Output 2: 
Input: 
4 
1 0 1 1 
0 0 0 1 
0 1 0 1 
1 1 0 0 
Output: 
6
#include<stdio.h>
#include <stdlib.h>

int main()
{
  int n,i,j,cnt=0;
  scanf("%d",&n);
  int mat[n][n],m[n][n];
  for(i=0;i<n;i++)
  {
      for(j=0;j<n;j++)
      {
          scanf("%d",&mat[i][j]);
      }
  }
  for(i=0;i<n;i++)
  {
      for(j=0;j<n;j++)
      {
          if(mat[i][j]!=mat[j][i])
          {
              cnt++;
          }
      }
  }
  printf("%d",cnt);         
}
