# Exercise 5: Create an inner function to 
# calculate the addition in the following way

# Create an outer function that will accept 
# two parameters, a and b
# Create an inner function inside an outer 
# function that will calculate the addition of a and b
# At last, an outer function will 
# add 5 into addition and return it
def outer_func(a:int,b:int):
    def inner_func(a,b):
        return a+b
    result = inner_func(a,b)
    return result+5

def main():
    if __name__=="__main__":
        a = int(input("Input a: "))
        b = int(input("Input b: "))
        print(outer_func(a,b))

main()