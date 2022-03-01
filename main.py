'''' Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) 
until the sum is at least equal to the limit set by the user.
In addition to the result it should also print out the calculation performed:
Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

''''


limit = int(input("Limit: "))
a = 1
n = 1
consecutive_sum = "The consecutive sum: 1 "


while a < limit:
    n = n + 1
    a = a + n 
    consecutive_sum += f"+ {n} "

consecutive_sum += f"= {a}"
print(consecutive_sum)
