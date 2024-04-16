# Print the following pattern
"""""
numbers = [1,2,3,4,5]
for number in numbers:
    for i in numbers:
        print(number)
"""""     
num = int(input("Enter number: "))
for i in range(num):
    for j in range(i):
        print(i, end=' ')
    #print("\n")
    print("")

"""""   
for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
"""""