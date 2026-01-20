# Exercise 5: Remove items from the set at once
# Write a Python program to remove items 10, 20, 30 from the following set at once.

# Given:

# set1 = {10, 20, 30, 40, 50}

# Expected output:

# {40, 50}

def main():
    set1 = {10, 20, 30, 40, 50}
    remove_set:set = {10,20,30}
    set1.difference_update(remove_set)
    print(set1)
if __name__=="__main__":
    main()