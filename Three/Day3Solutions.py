counter = 0
inc = None

def check_for_tree(line,move_down,pos):
    global line_num
    if line_num == move_down:
        global inc
        inc=True
        try:
            if line[pos] == '#':
                global counter
                counter += 1
        except:
            line = line + line
            check_for_tree(line, move_down, pos)
        line_num = 1
    else:
        global inc
        inc=False
        line_num += 1

def init_sled(move_right, move_down):
    with open('Day3_input') as file:
        pos = 0
        for line in file:
            line = line.strip()
            check_for_tree(line,move_down, pos)
            if inc:
                pos += move_right
            global counter
        return(counter)

line_num=1
t1 = init_sled(1,1)

counter = 0
line_num =1
t2 = init_sled(3,1)

counter = 0
line_num =1
t3 = init_sled(5,1)

counter = 0
line_num =1
t4 = init_sled(7,1)

counter = 0
line_num =2
t5 = init_sled(1,2)

all_trials = t1 * t2 * t3 * t4 * t5
print(all_trials)
