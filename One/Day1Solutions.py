
expenses = []

with open('DayOne_input') as file:
    for line in file:
        expenses.append(int(line.strip()))

for exp in expenses:
    check = 2020 - exp
    if check in expenses:
        print(check, exp)
        print (check * exp)
        break

tup = None
for exp in expenses:
    if tup:
        break
    sum_left = 2020 - exp
    for exp2 in expenses:
        check = sum_left - exp2
        if  check in expenses :
            tup = (check,exp, exp2)
            print(tup)
            print(check * exp * exp2)
            break

