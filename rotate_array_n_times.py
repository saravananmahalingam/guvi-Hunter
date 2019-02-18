# rotate
a,b=map(int,input().split())
c=list(map(int,input().split()))
d=c[b:]+c[:b]
print(*d)
