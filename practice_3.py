#Print characters from a string that are present at an even index number
def print_index_string(string):
    print("Printing only even index chars: ")
    length = len(string)
    for s in range(0, length, 2):
        print(string[s])

string = input("Enter string: ")
print_index_string(string)