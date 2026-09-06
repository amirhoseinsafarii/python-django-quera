
inputNumber = int(input())
strList = list()

for i in range(inputNumber):
    j=input()
    strList.append(j)


max_distinct_chars = 0
for i in strList:
    distinct_chars = ''

    for j in i:
        if j not in distinct_chars :
            distinct_chars += j


    max_distinct_chars = max(max_distinct_chars, len(distinct_chars))


print(max_distinct_chars)