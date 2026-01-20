# Exercise 5: Swap two tuples in Python
# Given:

# tuple1 = (11, 22)
# tuple2 = (99, 88)

# Expected output:

# tuple1: (99, 88)
# tuple2: (11, 22)
def swap(tuple1,tuple2):
    tuple1List = list(tuple1)
    tuple2List = list(tuple2)
    #print(tuple1List + tuple2List)
    tempList:list = [element for element in tuple1List]
    tuple1List.clear()
    tuple1List = [x for x in tuple2List]
    print(tuple(tuple1List))
    tuple2List.clear()
    tuple2List = [x for x in tempList]
    print(tuple(tuple2List))
def main():
    tuple1 = (11, 22)
    tuple2 = (99, 88)
    # Very simple
    # tuple1, tuple2 = tuple2, tuple1
    swap(tuple1,tuple2)

if __name__=="__main__":
    main()