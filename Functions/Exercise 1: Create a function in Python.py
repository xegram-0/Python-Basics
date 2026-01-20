# Exercise 1: Create a function in Python
# Write a program to create a function that takes two arguments,
# name and age, and print their value.

def function(name:str, age:str):
    print(f"Hello {name}, you are {age} years old.")
def main():
    if __name__=="__main__":
        name = input("Enter name: ")
        age = input("Enter age: ")
        function(name, age)
    
main()