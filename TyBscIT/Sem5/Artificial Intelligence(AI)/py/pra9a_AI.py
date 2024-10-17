def associative_law_addition(a,b,c):
    lhs = (a+b)+c
    rhs=a+(b+c)
    if lhs ==rhs:
        return True
    else:
        return False
def asssociative_law_product(a,b,c):
        lhs=(a*b)*c
        rhs=a*(b*c)
        if lhs==rhs:
            return True
        else:
            return False
a,b,c = 5,3,2
result1 = associative_law_addition(a, b, c)
result2 = associative_law_addition(a, b, c)
if result1:print("Associative Law holds for (a+b)+c = a+(b+c)")
else:
    print("Associative Law does not hold for (a+b)+c = a+(b+c)")
if result2:
    print("Associative Law holds for (a*b)c = a (b*c)")
else:
    print("Associative Law does not hold for (a*b)c = a (b*c)")