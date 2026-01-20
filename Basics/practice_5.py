# Check if the first and last number of a list is the same

def is_first_last_the_same(given_list):
    if (given_list[0]==given_list[-1]):
        return True
    else:
        return False

numberOflist = int(input("How many numbers in the list: "))
given_list= []
for i in range(numberOflist):
    #given_list[i] = int(input("Input", i, "number: "))
    given_list.append(input("Enter number: "))
print(given_list)
print(is_first_last_the_same(given_list))