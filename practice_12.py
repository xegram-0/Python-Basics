# Calculate income tax for the 
# given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

income = int(input("Give me your $$$: "))
tax_num = 0
# This is very specific program
if (income-10000) > 0:
    if (income-20000) > 0:
        remaining = income - 20000
        tax_num = 10000*0 + 10000*0.1 + remaining*0.2
    else:
        tax_num = 10000*0 + (income-10000)*0.1
else:
    tax_num = 10000*0
print("Here is how much you own us:", tax_num,"$")