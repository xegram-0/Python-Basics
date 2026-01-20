# Exercise 4: Unpack the tuple into 4 variables
# Write a program to unpack the following tuple into four variables and display each variable.

# Given:

# tuple1 = (10, 20, 30, 40)

# Expected output:

# tuple1 = (10, 20, 30, 40)
# # Your code
# print(a) # should print 10
# print(b) # should print 20
# print(c) # should print 30
# print(d) # should print 40

def make_variables(tuple1:tuple):
    var1, var2, var3, var4 = tuple1[0], tuple1[1], tuple1[2], tuple1[3]
    # a, b, c, d = tuple1
    print(var1)
    print(var2)
    print(var3)
    print(var4)

def main():
    tuple1 = (10, 20, 30, 40)
    make_variables(tuple1)
if __name__=="__main__":
    main()