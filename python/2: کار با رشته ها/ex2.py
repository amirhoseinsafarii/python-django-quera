
k = int(input())
passw = input()


cnt = 0
for i in range(k):
    roller = input()
    ind = roller.find(passw[i])

    if len(roller[0:ind]) > len(roller[ind+1:]) :
        cnt = cnt  + len(roller[ind:])

    elif len(roller[0:ind]) <= len(roller[ind+1:]):
        cnt = cnt + len(roller[0:ind])
 
print(cnt)