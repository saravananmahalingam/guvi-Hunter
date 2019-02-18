# rotated count
int(input())
count=0
b=list(map(int,input().split()))
c=list(map(int,input().split()))
for i in range(len(b)):
	d=b[i:]+b[:i]
	count=count+1
	if d==c:
		print(count-1)
