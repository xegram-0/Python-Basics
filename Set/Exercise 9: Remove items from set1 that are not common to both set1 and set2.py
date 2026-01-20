# Exercise 9: Remove items from set1 that are not common to both set1 and set2
# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# Expected output:

# {40, 50, 30}

def main():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.intersection_update(set2)
    print(set1)
if __name__=="__main__":
    main()