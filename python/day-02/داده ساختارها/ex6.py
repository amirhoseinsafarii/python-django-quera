from collections import Counter

cnt = int(input())


employee_list= {}

for i in range(cnt):
    employeeName, employeeLastname = input().split(" ")
    employee_list[i] = employeeName


countOfname = dict(Counter(employee_list.values()))

print(max(countOfname.values()))


