pw_w_cond = []

with open('Day2_input') as file:
    for line in file:
        pw_w_cond.append(line.strip())

counter = 0
for item in pw_w_cond:
    r , val , pw = str(item).split()
    low,high = r.split('-')
    letter = val[0]
    num = pw.count(letter)
    if num >= int(low) and num <= int(high):
        counter += 1

print(counter)


counter = 0
for item in pw_w_cond:
    check = 0
    r , val , pw = str(item).split()
    first, second = r.split('-')
    letter = val[0]
    ind1 = int(first) - 1
    ind2 = int(second) -1
    if pw[ind1] == letter:
        check += 1
    if pw[ind2] == letter:
        check += 1
    if check == 1:
        counter += 1
print(counter)

