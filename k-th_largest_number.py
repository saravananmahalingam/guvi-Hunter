# b th largest number
a,b=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
c.reverse()
print(c[b-1])
