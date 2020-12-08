inst =  []
indexes_visited = []
accumulator = 0
bit = False
with open('Day8_input') as file:
    for line in file:
        line = line.strip()
        inst.append(line)


def control(idx):
    try:
        code = inst[idx].split(' ')
    except:
        return
    global indexes_visited
    global bit
    if idx not in indexes_visited:
        bit = True
        indexes_visited.append(idx)
        if code[0] == 'nop':
            new_index = int(idx) +1
            control(new_index)
        elif code[0] == 'acc':
            global accumulator
            arith = code[1]
            sign = arith[0]
            if sign == '+':
                accumulator += int(arith[1:])
            else:
                accumulator -= int(arith[1:])
            new_index = int(idx) +1
            control(new_index)
        else:
            inc = code[1]
            sign = inc[0]
            if sign == '+':
                new_index = int(idx) + int(inc[1:])
            else:
                new_index = int(idx) - int(inc[1:])
            control(new_index)
    else:
        bit = False
        return


control(0)
print(accumulator)
accumulator=0

for index, each in enumerate(inst):
    bit = None
    if each[:3] == 'jmp':
        inst[index] = each.replace('jmp', 'nop')
        control(0)
        if bit:
            print(accumulator)
        indexes_visited = []
        accumulator =0
        inst[index] = each.replace('nop', 'jmp')
    elif each[:3] == 'nop':
        inst[index] = each.replace('nop', 'jmp')
        control(0)
        if bit:
            print(accumulator)
        indexes_visited = []
        accumulator =0
        inst[index] = each.replace('jmp', 'nop')

