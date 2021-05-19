def Solve(N,K,P,arr):
  for i in range(N):
    arr[i].insert(0,0)
    for j in range(1,K+1):
      arr[i][j]=arr[i][j]+arr[i][j-1]

  dp=[0]*(P+1)
  for i in range(N):
    new_dp=[0]*(P+1)
    for j in range(P+1):
      for z in range(min(K,j)+1):
        new_dp[j]=max(new_dp[j],arr[i][z]+dp[j-z])
    dp=new_dp
  
  return dp[-1]



T=int(input().strip())
for t in range(T):
	N,K,P=input().split(" ")
	N=int(N)
	K=int(K)
	P=int(P)
	arr=[]
	for _ in range(N):
		ent=list(map(int,input().split(" ")))
		arr.append(ent)
	print("Case #"+str(t+1)+": "+str(Solve(N,K,P,arr)))

