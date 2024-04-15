def print_the_sum(n):
    sum = 0
    previous_num = 0
    for num in range(n):
        sum = previous_num + num
        print("Current number", num, "Previous number", previous_num, "Sum", sum)
        #sum = previous_num + num
        previous_num = num
        
n = int(input("Input the range: "))
print_the_sum(n)