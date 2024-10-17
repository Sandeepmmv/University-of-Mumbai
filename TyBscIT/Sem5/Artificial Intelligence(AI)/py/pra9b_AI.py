def distributive_law_addition(a,b,c):
    lhs=a*(b+c)
    rhs=(a*b)+(a*c)
    if lhs == rhs:
        return True
    else:
        return False
def distributive_law_substraction(a, b, c):
    lhs=a*(b-c)
    rhs=(a*b)-(a*c)
    if lhs == rhs:
        return True
    else:
        return False
a,b,c=5,3,2
result1= distributive_law_addition(a, b, c)
result2= distributive_law_substraction(a, b, c)
if result1: 
    print("Distributive Law holds for a*(b+c) = (a*b) + (a*c)")
else:
    print("Distributive Law does not hold for a*(b+c) = (a*b)+(a*c)")
if result2:
    
    print("Distributive Law holds for a*(b-c) = (a*b) - (a*c)")
else:
        
    print("Distributive Law does not hold for a*(b-c) = (a*b) - (a*c)")