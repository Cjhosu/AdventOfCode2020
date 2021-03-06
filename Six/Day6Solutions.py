import numpy as np
count = 0
with open('Day6_sample') as file:
    group = []
    for line in file:
        if line != '\n':
            line = line.strip()
            for each in line:
                group.append(each)
        else:
            ary = np.array(group)
            unq = np.unique(ary)
            count += len(unq)
            group = []
    else:
        ary = np.array(group)
        unq = np.unique(ary)
        count += len(unq)
        group = []

print(count)

count = 0
with open('Day6_input') as file:
    group = []
    person = []
    for line in file:
        if line != '\n':
            person = line.strip()
            group.append(person)
        else:
            full = ''
            for st in group:
                full += st
            for each in group[0]:
                if full.count(each) == len(group):
                    count += 1
            group = []
    else:
        full = ''
        for st in group:
            full += st
        for each in group[0]:
            if full.count(each) == len(group):
                count += 1
        group = []

print(count)
