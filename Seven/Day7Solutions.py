import re

with open('Day7_input') as file:
    full = {}
    for line in file:
        rule = line.strip()
        rule = rule.split('contain')
        parent = rule[0]
        child = rule[1]
        lst_child = child.split(',')
        cln_lst = []
        for each in lst_child:
            each = re.sub('bag.*', '',each)
            each = each.strip(' ')
            cln_lst.append(each)
        child_dict= {}
        if cln_lst[0] != 'no other':
            for each in cln_lst:
                child_dict[each[2:]] = each[0]
        else:
            child_dict[''] = ''

        full[parent[:-6]] = child_dict


recurlist= []
def recur(colo):
    for k in full:
        if colo in full[k]:
            recurlist.append(k)
            recur(k)

recur('shiny gold')
recurset = set((recurlist))
print(len(recurset))

counter = 0
inner = 0

def recurcount(colo, num):
    bags = full[colo]
    global inner
    for k,v in bags.items():
        if v.isdigit():
            inner = int(v) * int(num)
            global counter
            counter += int(v) * int(num)
            recurcount(k, inner)

recurcount('shiny gold', 1)
print(counter)
