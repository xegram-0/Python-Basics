# Write a Program to extract each digit 
# from an integer in the reverse order

og_num = str(input("Enter a number: "))
rv_num = ''

for i in range(1, len(og_num)+1):
    rv_num+=og_num[-i]
    #print(rv_num, end='')
#print("\n")
#print("Reverse number:", int(rv_num))
print("Reverse number:", rv_num)

'''
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
'''