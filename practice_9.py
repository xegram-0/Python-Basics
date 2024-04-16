# Check Palindrome Number
og_num = str(input("Original number: "))
rv_num = ''

# We start at -1 so we lost the i = 0 case
# By adding 1 at the end, the last number is included.
for i in range(1, len(og_num)+1):
    #rv_num.append(og_num[-i])
    rv_num+=og_num[-i]
    #print(rv_num)
'''
# reverse the given number using math
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
'''
og_num = int(og_num)
rv_num = int(rv_num)
if (og_num == rv_num):
    print("This is panlindrome number.")
else:
    print("Not a panlindrome number.")