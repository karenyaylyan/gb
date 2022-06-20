import functools


def type_logger(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args)
        args_type = ', '.join((f'{arg}: {type(arg)}' for arg in args))
        kwargs_type = ', '.join((f'{value}: {type(value)}' for value in kwargs.values()))

        if args_type and kwargs_type:
            all_type = ', '.join([args_type, kwargs_type])
        elif args_type:
            all_type = args_type
        else:
            all_type = kwargs_type

        print(f'{func.__name__}({all_type}) -> {type(result)}')
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
