def zero_check(function):
    def check(x, y):
        if y == 0:
            return('y is zero')
        return function(x, y)

    return check


def zero_call(fix):
    def sub(x, y):
        if x == 0:
            return('x is zero')
        return fix(x, y)

    return sub


@zero_check
def add(x, y):
    return x + y
@zero_call
def sub(x, y):
    return x - y


print(add(12,78))
print(sub(89,56))
