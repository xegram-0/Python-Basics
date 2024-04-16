# Create a new list from two list using the following condition
# A new list such that the new list should contain odd numbers 
# from the first list and even numbers from the second list.

list1 = [10,20,25,30,35]
list2 = [40,45,60,75,2]
fin_list = []

for i in range(len(list1)):
    if list1[i]%2 != 0:
        fin_list.append(list1[i])
        print("From list 1", fin_list)
for i in range(len(list2)):
    if list2[i]%2 == 0:
        fin_list.append(list2[i])
        print("From list 2", fin_list)


#print("Result list ", fin_list)
print("Result list ", sorted(fin_list))