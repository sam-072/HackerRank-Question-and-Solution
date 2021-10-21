import sys
l=[]
for i in range(3):
    l.extend(list(map(int,input().split())))
x=[[8,1,6,3,5,7,4,9,2], [6,1,8,7,5,3,2,9,4], [4,9,2,3,5,7,8,1,6], [2,9,4,7,5,3,6,1,8],[8,3,4,1,5,9,6,7,2],[4,3,8,9,5,1,2,7,6],[6,7,2,1,5,9,8,3,4],[2,7,6,9,5,1,4,3,8]]
c=sys.maxsize
for i in range(8):
    t=0
    for j in range(9):
        t+=abs(x[i][j]-l[j])
    if t<c:
        c=t
print(c)



