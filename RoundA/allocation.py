
def solve(N,B,ent,t):
	ent=sorted(ent)
	salida=[]
	i=0
	acum=0
	while True:
		if acum+ent[i]<=B:
			print(ent[i])
			i=i+1
			acum=acum+ent[i]
		else:
			break

	print("Case #"+str(t+1)+": "+str(i))
		




T=int(input().strip())
for t in range(T):
	N,B=input().split(" ")
	N=int(N)
	B=int(B)
	ent=list(map(int,input().split(" ")))
	solve(N,B,ent,t)
