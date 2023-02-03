'''
Do you remember Noddy? You may or may not, but he has definitely heard of you. You're getting quite famous 😎

After your most recent rescue of Nobita (seriously, where did he get those mushrooms?), the entire cartoon universe wants to throw you a party.

It's going to be on a special island, and Noddy is your special driver - he will be flying you in his own airplane.


There's only 1 problem. He doesn't have enough fuel. The journey is long and you will need a lot of fuel.

Noddy's vehicle has 2 issues:

It needs exactly F amounts of fuel to fly this distance - not more and not less.
At a particular time, it cannot increase the fuel by more than K
There are N fuel stations on the way: each having A1 A2..... AN amount of fuel.

You have to tell us whether it is possible to fill the tank up to exactly F amounts.

Input Format
The first line contains T, the number of test cases. Each test case contains:
N, followed by N numbers denoting the amount of fuel at the ith station
F - the target fuel that you must reach
K - your limit for max fuel at one station
Output Format
Print Yes if you can fill with the given stations and capacities. Otherwise, print No

Sample Input
3
6 6 10 3 2 2 1
7
5
5 6 10 3 2 2
7
1
6 8 10 3 9 7 4 
2
10
Sample Output
Yes
No
No
Explanation

In the first case, 7 can be reached by taking 3, 2 and 2
In the second case, since we can never pick up more than 1, we can't reach 7
There is no way of reaching 2

'''
from itertools import combinations
t=int(input())
for _ in range(t):
    fa=list(map(int,input().split()))[1:]#fa stands for fuel available
    tf=int(input())#tf stnds for target fuel
    mfl=int(input())#mfl stands for max fuel limit at aone station
    lenf=len(fa)
    sb=[]
    dfa=sorted(fa)
    lend=len(dfa)
    jsb=100
    for i in range(lend):
        if dfa[i]>mfl:
            dfa=dfa[:i]
            break
    #print('dfa---',dfa)
    for i in range(1,lenf):
        sb.extend(list(combinations(dfa,i)))
    for ele in sb:
        if sum(list(ele))==tf:
            jsb=10
            break
    if jsb==10:
        print('Yes')
    else:
        print('No')
    





