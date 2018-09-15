def add_numbers(*args):
    result = 0
    for num in args:
        if not isinstance(num, int):
            raise ValueError
        result = num + result