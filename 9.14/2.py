def fruit_color(color):
    '''

    :param color: color of fruit
    :return: fruit that matches the color
    '''
    if color == 'red':
        return 'apple'
    elif color == 'yellow':
        return 'banana'
    elif color == 'green':
        return 'melon'
    else:
        return "I don't know"

help(fruit_color)