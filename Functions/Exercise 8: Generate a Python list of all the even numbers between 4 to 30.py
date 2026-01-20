# Exercise 8: Generate a Python list of 
# all the even numbers between 4 to 30

# Expected Output:

# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
def generateList(start:int, end:int):
    evenList:list = []
    for i in range(start,end+1):
        if i%2 == 0:
            evenList.append(i)
    print(evenList)
def main():
    if __name__=="__main__":
        start = int(input("Enter starting number of the list: "))
        end = int(input("Enter ending number of the list: "))
        generateList(start,end)
        #print(list(range(4,30,2)))
main()