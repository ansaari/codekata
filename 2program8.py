f,g=(raw_input()).split(" ")
f=int(f)
g=int(g)
for i in range(f,g):
    h= len(str(i))
    sum = 0
    j = i
    while j>0:
        k=j%10
        sum+= k**h
        j//=10
        if i == sum:
            print(i)
