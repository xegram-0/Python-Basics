# Write a function called exponent(base, exp) that 
# returns an int value of base raises to the power of exp.

def exponent(base, exp):
    '''''
    i = 0
    while(i <= exp):
        result = result * base
        i+=1
    return result
    '''''
    #return base**exp
    result = base ** exp
    print(base, "raises to the power of", exp, "is", result)
    print("i.e.", end=' ')
    for i in range(exp):
        print(base, end='')
        if(i < exp-1):
            print("*", end='')
    print(" =",result)
    # No need since the input is converted to int
    # which would lead to error
    #return isinstance(base,int)



while True:
    base = int(input("Enter base: "))
    exp = int(input("Enter exp: ")) 
    if (exp > 0):
        exponent(base, exp)
        break
    else:
        #print("Exp is negative.")
        print("Exp must be positive.")
        continue

