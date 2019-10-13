'''
Source: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

Level: Easy

Date: 5th July, 2019

'''

'''
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes jumps while the second takes .

Function Description

Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

c: an array of binary integers
Input Format

The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .

Constraints

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0
Sample Output 0

4
Explanation 0: 
Emma must avoid  and . She can win the game with a minimum of  jumps:

jump(2).png

Sample Input 1

6
0 0 0 0 1 0
Sample Output 1

3
Explanation 1: 
The only thundercloud to avoid is . Emma can win the game in  jumps:

jump(5).png
'''

#Solution

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cumulusClouds = []
    for index,cloud in enumerate(c):
        if cloud == 0:
            cumulusClouds.append(index)
            
    i = 0
    count = -1
    while i < len(cumulusClouds):
        if i == len(cumulusClouds) - 2:
            count += 2
            break
        elif i == len(cumulusClouds) - 1 or cumulusClouds[i + 2] - cumulusClouds[i] == 2:
            count += 1
            i = i + 2
        else:
            count+=1
            i = i + 1

    
    return count 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
