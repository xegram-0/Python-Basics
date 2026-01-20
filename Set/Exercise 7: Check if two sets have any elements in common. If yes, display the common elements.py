# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# Expected output:

# Two sets have items in common
# {10}


def main():
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}
    if set1.isdisjoint(set2):
        print("Two sets have no item in common.")
    else:
        set3:set = set1.intersection(set2)
        print(f"Two sets have item in common \n {set3}")

if __name__=="__main__":
    main()