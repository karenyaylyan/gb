def val_checker(func_check):

    def _val_checker(func):

        def wrapper(*args, **kwargs):
            for arg in args:
                if not func_check(arg):
                    raise ValueError(f'wrong val {arg}')
            for arg in kwargs.values():
                if not func_check(arg):
                    raise ValueError(f'wrong val {arg}')

            result = func(*args, **kwargs)
            return result

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(*args, **kwargs):
    return 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)
