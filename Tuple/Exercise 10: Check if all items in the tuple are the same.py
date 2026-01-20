# Exercise 10: Check if all items in the tuple are the same
# tuple1 = (45, 45, 45, 45)

# Expected output:

# True
def check_same(tuple1):
    value:int = tuple1[0]
    for num in tuple1:
        if num != value:
            print("False")
            break
    else:
        print("True")
def main():
    tuple1 = (45, 45, 45, 45)
    check_same(tuple1)
    # all(i == t[0] for i in t)
if __name__=="__main__":
    main()