def polysum(n, s):
    '''
    char: n number of polygon sides
    aStr: s lenght of each side

    returns: sum of the area and square of the perimeter of polygon
    '''
    # Your code here
    import math

    area = (0.25*n*(s**2)) / (math.tan(math.pi / n))

    per = s * n

    return round((area + per ** 2), 4)
