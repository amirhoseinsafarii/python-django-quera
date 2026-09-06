import json

n = int(input())

cDict = {}
results = []
for item in range(n):
    command = input()
    if command.startswith("print"):
        var, value = command.split(" ")
        result = eval(value, {}, cDict)
        results.append(result)
        continue

    var, value = command.split(":=")
    value = value.strip()
    var = var.strip()
    value = json.loads(value)
    cDict[var] = value

for result in results:
    print(result)
