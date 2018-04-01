# Raise exception to indicate situation instead of returning None

def safe_int(str_obj):
    try:
        retval = int(str_obj)
    except (ValueError, TypeError) as reason:
        raise reason
    return  retval


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

if __name__ == '__main__':
    x, y = '5', 'rrr'
    a = safe_int(x)
    b = safe_int(y)
    if isinstance(a, int) and isinstance(b, int):
        try:
            result = divide(a, b)
        except (ValueError, TypeError):
            print ('invalid inputs')
        else:
            print ('result is %.1f' % result)

