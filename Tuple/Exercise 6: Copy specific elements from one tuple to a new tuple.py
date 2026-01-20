# Exercise 6: Copy specific elements from one tuple to a new tuple
# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

# Given:

# tuple1 = (11, 22, 33, 44, 55, 66)

# Expected output:

# tuple2: (44, 55)

def copy_tuple(tuple1):
    tuple2List:list = []
    if 44 in tuple1:
        tuple2List.append(44)
    if 55 in tuple1:
        tuple2List.append(55)
    print(f"tuple2: {tuple(tuple2List)}")
def main():
    tuple1 = (11, 22, 33, 44, 55, 66)
    copy_tuple(tuple1)
    #tuple2 = tuple1[3:-1]
if __name__=="__main__":
    main()