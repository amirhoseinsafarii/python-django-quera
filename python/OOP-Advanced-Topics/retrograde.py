class Reverse:
    def __init__(self, data):
        self._data = list(data)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._data) == 0:
            raise StopIteration

        # for i in range(len((self._data))):
        #     index = i

        return self._data.pop()


ls = [10, 20, 30]

print("Reverse iteration")
for it in Reverse(ls):
    print(it)

print("Original list:")
print(ls)
