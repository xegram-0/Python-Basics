#  Display numbers divisible by 5 from a list
def is_divided_by_5(list_num):
    #length = len(list_num)
    #for i in range(length):
    for i in list_num:
        #if (list_num[i]%5 == 0):
            #print(list_num[i])
        if (i%5 == 0):
            print(i) 
    #print("The end of the program!")

num_list = int(input("How many numbers in the list: "))
list_num = []
for i in range(num_list):
    list_num.append(int(input("Enter number: ")))
#print(list_num)
is_divided_by_5(list_num)