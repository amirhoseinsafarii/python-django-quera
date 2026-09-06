
list1 = list()
while True:
    n = int(input())
    if n == 0 :
        break
    list1.append(n)

list1.reverse()
for i in list1:
    print(i)