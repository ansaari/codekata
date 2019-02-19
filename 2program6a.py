u,v=raw_input().split()
u=int(u)
v=int(v)
for m in range(u+1,v):
    if m>1:
        for i in range(2,m):
         if(m%i==0):
          break
        else:
         print(m),
