p , d = input().split()
p = int(p)
d = int(d)

num = 1
while True:
    m = d * num
    b = m % p
    if b <= p/2 :
        print(m)
        break
    else:
        num = num+1


