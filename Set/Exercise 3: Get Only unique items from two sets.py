# Exercise 3: Get Only unique items from two sets
# Write a Python program to return a new set with unique items from both sets by removing duplicates.

# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# Expected output:

# {70, 40, 10, 50, 20, 60, 30}



def main():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    #set3:set = set1.symmetric_difference(set2)
    set3 = set1.union(set2)
    print(set3)
if __name__=="__main__":
    main()