def sumValues(a, b, *others):
    retValue = a+b

    for other in others:
        retValue = retValue + other

    return retValue    
