class ExceptionProxy(Exception):
    def __int__(self, message, function):
        self.function = function
        self.message = message


def transform_exceptions(func_ls: list) -> list[ExceptionProxy]:
    ExceptionProxyList = []
    for func in func_ls:
        ExceptionProxyObject = ExceptionProxy()

        try:
            func()
        except Exception as e:
            ExceptionProxyObject.function = func
            ExceptionProxyObject.message = str(e)
            ExceptionProxyList.append(ExceptionProxyObject)
        else:
            ExceptionProxyObject.function = func
            ExceptionProxyObject.message = "ok!"
            ExceptionProxyList.append(ExceptionProxyObject)
    return ExceptionProxyList


def f():
    return 1 / 0


def g():
    pass


exceptions_info = transform_exceptions([f, g])

for item in exceptions_info:
    print(f"function: {item.function}")
    print(f"function name: {item.function.__name__}")
    print(f"message: {item.message}")
    print("-" * 10)
