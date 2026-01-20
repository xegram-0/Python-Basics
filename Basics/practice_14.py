# Print a downward Half-Pyramid 
# Pattern of Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

num = int(input("How many rows: "))
# pay attention to this
for i in range(num+1,0,-1):
    for j in range(i-1):
        #print(j, end='')
        print('*' ,end=' ')
    print("\t")