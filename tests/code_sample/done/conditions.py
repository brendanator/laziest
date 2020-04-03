class CustomException(Exception):
    pass


def one_condition_standard_exception(arg1):
    if arg1 == '1':
        raise Exception('we hate 1')
    elif arg1 > 2:
        print(f'{arg1} more when 2')
    else:
        return arg1


def one_condition_custom_exception(arg1):
    if arg1 == '1':
        raise CustomException('we hate 1')
    elif arg1 > 2:
        print(f'{arg1} more when 2')
    else:
        return arg1


def one_condition_custom_exception_and_return_binary_op(arg1, arg2=123, arg3=123):
    if arg1 == '1':
        raise CustomException('we hate 1')
    elif arg1 > 2:
        print(f'{arg1} more when 2')
        return arg1
    var = 1
    alias = var
    return arg1 * arg2 + arg3, alias * arg1 * alias - 2

def one_condition_custom_exception_and_return_binary_op_and_key(arg1, arg2, arg3):
    if arg1 == '1':
        raise CustomException('we hate 1')
    elif arg2[3] > 2:
        print(f'{arg2[3]} more when 2')
    var = 1
    alias = var
    return arg1 * arg2[3] + arg3['number'], alias * arg1 * alias - 2


def body_in_conditions(chunk):
    if '=' in chunk:
        key, _ = chunk.split('=', 1)
        return key


def include_symbol_in_str_tuple(chunk):
    if '=' in chunk:
        key, val = chunk.split('=', 1)
        return key, val


def multiply_conditions(arg1, arg2):
    if arg1 or arg2:
        return True
