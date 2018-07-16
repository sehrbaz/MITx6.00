def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) < 1:
        return False
    elif len(aStr) == 1 and char == aStr:
        return True
    elif len(aStr) == 1 and char != aStr:
        return False
    else:
        mid = len(aStr) // 2
        if aStr[mid] == char:
            return True
        elif char < aStr[mid]:
            aStr = aStr[:mid]
        else:
            aStr = aStr[mid:]
        return isIn(char, aStr)

print(isIn('l', 'knrs'))
