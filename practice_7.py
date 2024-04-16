# Return the count of a given substring from a string
#""""
def return_count(big_string,target_string):
    count = 0
    #a = 0
    b = len(target_string)
    # Don't understand why subtract 1 at this place
    #for i in range(len(big_string)-1):
    for i in range(len(big_string)):
        #"""""
        # Why b only is not working but i+b or i+4 works????
        if (target_string == big_string[i:(i+b)]):
            count+=1
            #a+=1
            #b+=1
        #"""""
        #count += big_string[i: i + 4] == target_string
    return count
#"""
big_string = input("Enter the string: ")
target_string = input("Enter the target string: ")
print(return_count(big_string, target_string))
#print(big_string.count(target_string))