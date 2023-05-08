'''
a b c
a c b
b a c
b c a
c a b
c b a
'''
def med3(a, b, c):
    if a >= b: # a b
        if b >= c: # a b c
            return b
        elif c >= a: # c a b
            return a
        else: # a c b
            return c
    elif a > c: # b a c
        return a
    elif b > c: # b c a
        return c
    else:
        return b
    '''
    b a c
    b c a
    c b a
    '''