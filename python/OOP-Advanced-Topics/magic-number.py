class Strint(int):

    def __lt__(self, other):
        num1 = self % 10
        num2 = other % 10
        return num1 < num2

    def __gt__(self, other):
        num1 = self % 10
        num2 = other % 10
        return num1 > num2

    def __le__(self, other):
        num1 = self % 10
        num2 = other % 10
        return num1 <= num2

    def __ge__(self, other):
        num1 = self % 10
        num2 = other % 10
        return num1 >= num2

    def __eq__(self, other):
        num1 = self % 10
        num2 = other % 10
        return num1 == num2

    def __ne__(self, other):
        num1 = self % 10
        num2 = other % 10
        return num1 != num2

    def __add__(self, other):
        str1 = str(self)
        str2 = str(other)
        result = str1 + str2
        return int(result)

    def __sub__(self, other):
        str1 = str(self)
        str2 = str(other)

        if not str1.endswith(str2):
            raise ValueError("The subtraction is not valid!")
        else:
            result = str1.removesuffix(str2)
            if result == "":
                result = 0
                return result
            else:
                return int(result)

    def __len__(self):
        return len(str(self))

    def __call__(self):
        return str(self)

    def __str__(self):
        digits = {
            "0": "۰",
            "1": "۱",
            "2": "۲",
            "3": "۳",
            "4": "۴",
            "5": "۵",
            "6": "۶",
            "7": "۷",
            "8": "۸",
            "9": "۹",
        }

        return "".join(digits.get(char, char) for char in int.__str__(self))
