#Remove first n characters from a string 
def remove_chars(string,n):
    print(string[n:])
    
your_string = input("Enter string: ")
while True:
    num_chars = int(input("Enter number of chars to be removed: "))
    if num_chars>len(your_string):
        print("n must be less than the length of the string!")
    else:
        remove_chars(your_string, num_chars)
        break
