# Exercise 6: Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

# A recursive function is a function that calls itself again and again.

# Expected Output:

# 55
def func_recursive(num:int):
    #print("Testing")
    #sum = 0
    # Not understand this part
    #if num !=1:
    # Would evaluate until num reaches 0 since that would be false
    if num: 
        return num + func_recursive(num-1)
    else:
        return 0
        

def main():
    if __name__=="__main__":
        print(func_recursive(10))

main()