def calcaulte(*args):
    '''

    :param args: number of int args should be less than or equal to two.
    :return: arg1 multiplied by arg2 if two args, otherwise square of arg1
    '''
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]
