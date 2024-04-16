# Print multiplication table from 1 to 10
rows = int(input("How many rows: "))

for i in range(1,rows+1):
    for j in range(1,11):
        print(i*j, end=' ')
    
    print("\t\t") # tab results
    
    #print("\n") # newline results