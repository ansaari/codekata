l=int(raw_input())
m=0
n=l
while l!=0:
    o=l%10
    m=m*10+o
    l=l/10
if m==n:
        print("yes")
else:
        print("no")
