g=int(raw_input())
h=0
for i in range (2,g//3):
    if(a%i==0):
        h=h+1
if(h<=0):
    print("yes")
else:
    print("no")
