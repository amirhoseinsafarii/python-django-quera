def decorator_builder(validator):
    def main_decorator(func):
        def decorator_wrapper(*args, **kwargs):
            if validator(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                return "error"

        return decorator_wrapper

    return main_decorator


def nonnegative_validator(x):
    return x >= 0


@decorator_builder(nonnegative_validator)
def square_root(x):
    return x**0.5


print(square_root(4))  # 2.0

print(square_root(-4))  # error
