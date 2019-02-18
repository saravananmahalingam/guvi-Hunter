# reverse the number
a=int(input())
b=list(map(int,input().split()))
b.reverse()
c=len(b)
for i in b:
	if i==b[c-1]:
		print(i,end="")
	else:
		print(i,end="->")
