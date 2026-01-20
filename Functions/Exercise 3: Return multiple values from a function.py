# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() 
# such that it can accept two variables and calculate addition 
# and subtraction. Also, it must return both addition 
# and subtraction in a single return call.
# Given:

# def calculation(a, b):
#     # Your Code

# res = calculation(40, 10)
# print(res)

# Expected Output

# 50, 30
def calculation(num1:int,num2:int):
    sum = num1 + num2
    subtraction = num1 - num2
    return sum, subtraction

def main():
    if __name__=="__main__":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        sum, subtraction = calculation(num1,num2)
        print(f"Sum is {sum} and subtraction is {subtraction}.")
main()
