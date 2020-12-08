inst =  []
indexes_visited = []
accumulator = 0
with open('Day8_sample') as file:
    for line in file:
        line = line.strip()
        inst.append(line)
    print(inst)


def control(idx):
   code = inst[idx].split(' ')
   print(code)
   if idx not in indexes_visited:
       indexes_visited.append(idx)
       if code[0] == 'nop':
           new_index = int(idx) +1
           control(new_index)
       elif code[0] == 'acc':
           arith = code[1]

control(0)
