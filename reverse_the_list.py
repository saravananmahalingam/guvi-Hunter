# reverse the number
a=int(input())
b=list(map(int,input().split()))
b.reverse()
c=len(b)
for i in range(c):
	if i==c-1:
		print(b[i],end="")
	else:
		print(b[i],end="->")
