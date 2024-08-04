def is_prime(func):
    def wrapper(*args):
        result1 = func(*args)
        d = 2
        while result1 % d != 0:
            d += 1
        if d == result1:
            return f'Простое\n{result1}'

        elif d < result1:
            return f'Составное\n{result1}'

    return wrapper


@is_prime
def sum_tree(*args):
    result = sum(args)
    return result


print(sum_tree(2, 3, 6))
