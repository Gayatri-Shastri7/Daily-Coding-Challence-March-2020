'''
Challenge #4 [InfyTQ] - Nobita & Doaremon
Doraemon and Nobita have called upon you. Will you turn them down? No, we wouldn't think so.

It seems Nobita has ingested some poisonous mushrooms (how did he get those mushrooms anyway?) - and has now not able to see clearly. Doraemon is usually very resourceful, but turns our he is allergic to mushrooms.


Nobita has a specific medicine to solve this problem. He tried to say the name of the medicine, but his sentences are jumbled beyond imagination.

Here is how you can help him:

His sentence is in the form of a very long word. mymedicinesarerighthere
You need to break this word down in the following way: m, ym ,edi ,cine ,sarer ,ighthe, re
Then take the first and last characters of the sub-words as long as the sub-word is longer than the previous sub-word: m, ym, ei, ce, sr, ie. Notice we don't touch re because it is shorter than the previous sub-word
The words on joining gives the name of Nobita's medicines: mymeicesrie
Input Format
The first line contains T, the number of test cases
This is followed by T strings (with length >=1)
Output format
Print the name of Nobita's medicines
Example Input:

3
mymedicinesarerighthere
isnobitaalive
testcasesoftenmakemuchmoresensethanthisone
Example Output:

mymeicesrie
isnoitl
testasofmachent
Note: Students coding in Java, please keep your class name as Main

All the best!


'''
t = int(input())



for i in range(t):

  s = input()

  i=0

  j=1

  k=2

  l=[]

  while s[i:j]!='':

    l.append(s[i:j])

    i=j

    j=min(j+k,len(s))

    k+=1



  for i in range(len(l)):

    if i ==0:

      print(l[i],end='')

    else:

      if len(l[i-1])<len(l[i]):

        print(l[i][0]+l[i][len(l[i])-1],end='')

      else:

        continue 

  print('')







