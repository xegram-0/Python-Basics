# Exercise 9: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]

# Expected Output:

# 24
def findingMax(theList:list):
    maxNum = theList[0]
    for i in theList:
        if i > maxNum:
            maxNum = i
        else:
            continue
    return maxNum
def main():
    if __name__=="__main__":
        theList = [4, 6, 8, 24, 12, 2]
        print(findingMax(theList))
        #print(max(theList))
main()