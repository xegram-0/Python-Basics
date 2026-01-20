# Exercise 2: Create a function with 
# variable length of arguments

# Function call:

# # call function with 3 arguments
# func1(20, 40, 60)

# # call function with 2 arguments
# func1(80, 100)

# Expected Output:

# Printing values
# 20
# 40
# 60


# Printing values
# 80
# 100

def func1(*num):
    print("Printing values:")
    for i in num:
        print(i)

def main():
    if __name__=="__main__":
        func1(20,40,60)
        func1(80,100)
main()