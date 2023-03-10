'''
Challenge #6 [EPAM] - Shinchan's Party Games
With your help, Noddy has been able to transport the both of you to the grand party on Party IslandTM

Over there, the games have begun. One such game is the maze game, which Shinchan has set up.


The maze looks like this:


In the maze, you start at the top left 1,1, and make your way down to n,n. At each step, you are only allowed 3 moves:

You can move to the right (east)
You can move down (south)
If you are on the left diagonal (row number and column number are same), then you can move down and right (south-east) in one move
However, you cannot move to the block if it is an obstacle. You can only move if there is a path. 1 denotes an obstacle and 0 the path.

You have to print the minimum number of steps to reach the destination (bottom-right) from the starting position (top-left).

In the above diagram, the minimum number of steps required is 3 steps:

Step 1: (1,1) -> (2,2)
Step 2: (2,2) -> (3,3)
Step 3: (3,3) -> (4,4)
Input format
The first line contains T the number of test cases
Each test case contains n and n, the number of rows and columns (it is always a square maze)
This is followed by n space separated numbers in n lines
Output format
For each test case, print the minimum number of steps required to reach the destination
Note: the start and destination will always be marked as 0 in the map

Example Input

2
3 3
0 1 1
1 0 1
0 0 0
4 4
0 0 0 1
0 0 1 0
0 0 1 0
1 0 0 0
Example Output

2
5
Explanation

In first case, move along the diagonal and you will reach the destination in 2 steps
The steps are: (1,1) -> (2,2); (2,2) -> (3,2); (3,2) -> (4,2); (4,2) -> (4,3); (4,3) -> (4,4)
Note: students coding in Java should keep their class name as Main


'''

t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    l=[]
    for i in range(m):
        l.append(list(map(int,input().split())))
    i,j=0,0
    cnt_1,cnt_2=0,0
    while(i!=m-1 or j!=n-1):
        if(i==j and l[i+1][j+1]==0):
            i+=1
            j+=1
        elif(i!=m-1 and l[i+1][j]==0):
            i+=1
        else:
            j+=1
        cnt_1+=1
    i,j=0,0
    while(i!=m-1 or j!=n-1):
        if(i==j and l[i+1][j+1]==0):
            i+=1
            j+=1
        elif(j!=n-1 and l[i][j+1]==0):
            j+=1
        else:
            i+=1
        cnt_2+=1
    print(min(cnt_1,cnt_2))

