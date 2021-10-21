# problem name : Sherlock and the Valid String
# problem link : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# Lvel : Medium 

s = input()
f = 26*[0]
for i in s:
    f[ord(i)-97]+=1
s=set()
for i in f:
    if i !=0 :
        s.add(i)
# print(s)
# print(f)
if len(s)==1:
    print("YES")
elif len(s) == 2:
    l=list(s)
    c1=f.count(l[0])
    c2=f.count(l[1])
    # print(l,c1,c2)
    if (abs(l[0]-l[1])==1 or (l[0]==1 and l[1]!=1) or (l[1]==1 and l[0]!=1)) and ( c1==1 or c2==1 ) and f.count(1)<=1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")