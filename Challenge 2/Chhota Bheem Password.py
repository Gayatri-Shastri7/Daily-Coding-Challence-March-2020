'''
Challenge #2 [WIPRO] - Chhota Bheem's Password
It seems many of you helped our Suppandi really well in the previous challenge. He was very impressed, and has referred you to Chhota Bheem. Unlike Suppandi, Chhota Bheem is very smart. He doesn't need your help, instead he wants to test you.


Chhota Bheem's notebook is encrypted with a secret password. He never remembers the password, because he uses a hint and a formula to generate the password.

The hint is a series of N positive numbers. Some of these numbers are purposely left blank, and these are denoted by -1

He tells you that the way to generate the password is:

First you need to fill in the blanks. If numbers on both sides of the blank are both odd, or are both even, then fill it with the absolute difference of both numbers.

However, if both the numbers different (i.e. one is odd and the other is even), in that case fill it with the floor of the arithmetic mean of the 2 numbers.

Second, after you have filled in the blanks, reduce all numbers by 1 except the last number and the numbers whose value is already 1.

Finally, print all the numbers without any spaces. That is the password.

Note: The blanks never appear at the start or end of the list. The blanks also never appear next to each other

Input Format
The first line contains T the number of test cases
The following T lines contains N followed by N numbers (all greater than 0). This is the hint as given by Chhota Bheem
Note: N>=3

Output Format
Print T passwords in a separate line
Example Input
3
5 9 -1 8 1 2
3 9 1 4
10 1 22 3 17 -1 5 -1 8 -1 10
Example Output
87712
814
12121611457110
Explanation

In the first case, the blank is replaced by (9+8) / 2 = 8.5, since we take floor, we take 8. Then all numbers are subtracted by 1 as per the conditions: 8 7 7 1 2. Finally, print: 87712
In the second case, there are no blanks to fill, so we just subtract 1 from applicable numbers. In this case, that is the first number 9. Thus we print 814
In the last case, the blanks are filled as follows:
1 22 3 17 12 5 6 8 2 10

Then, subtracting by 1:

1 21 2 16 11 4 5 7 1 10

And printing

12121611457110

Note: Users running code in Java should keep the class name as Main

All the best!

'''

import math
T=int(input())

for i in range(T):

  a = list(map(int,input().strip().split()))

  b=[]

  n=a[0]

  a.pop(0)

  for i in range(n):

    if(a[i]==-1):

      if(((a[i-1])%2==0 and (a[i+1])%2==0) or ((a[i-1])%2!=0 and (a[i+1])%2!=0)):

        a[i]= math.fabs((a[i-1]-a[i+1]))

      else:

        a[i]=(((a[i-1])+(a[i+1]))//2)

  for i in range(n-1):

      a[i]=a[i]-1

      b.append(a[i])

  b.append(a[n-1])

  for i in range(n):

    if(b[i]==0):

      b[i]=1

  for i in range(n):

    print(int(b[i]),end="")

  print()
