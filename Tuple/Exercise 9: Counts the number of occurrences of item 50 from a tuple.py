# Exercise 9: Counts the number of occurrences of item 50 from a tuple
# Given:

# tuple1 = (50, 10, 60, 70, 50)

# Expected output:

# 2
def count_50(tuple1):
    count:int = 0
    for num in tuple1:
        if num == 50:
            count += 1
    print(count)

def main():
    tuple1 = (50, 10, 60, 70, 50)
    count_50(tuple1)
    # print(tuple1.count(50))
if __name__=="__main__":
    main()