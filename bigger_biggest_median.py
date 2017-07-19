def bigger(a,b):
    if a>b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,b,c)

def median:(a,b,c):
    big - biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)

def lesser(a,b):
    if a<b:
        return a
    else:
        return b
def least(a,b,c):
    return lesser(a,lesser(b,c))

def set_range(a,b,c):
     return biggest(a,b,c) - least(a,b,d)
