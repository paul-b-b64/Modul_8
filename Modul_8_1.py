def add_everything_up(a, b):
    try:
        result = a + b
    except:
        if isinstance(a, float or int):
            a = str(a)
        if isinstance(a, str):
            b = str(b)
        result = f'{a}{b}'
    finally:
        return result



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
