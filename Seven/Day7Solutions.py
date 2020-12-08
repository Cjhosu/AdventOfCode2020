import re

with open('Day7_input') as file:
    full = {}
    for line in file:
        rule = line.strip()
        rule = rule.split('contain')
        outer = rule[0]
        inner = rule[1]
        lst_inner = inner.split(',')
        lst = []
        for each in lst_inner:
            each = re.sub('bag.*', '',each)
            each = each.strip(' ')
            lst.append(each)
        dic= {}
        if lst[0] != 'no other':
            for each in lst:
                dic[each[2:]] = each[0]
        else:
            dic[''] = ''

        full[outer[:-6]] = dic


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
        if v.isdigit():
            recurcount(k, inner)


recurcount('shiny gold', 1)
print(counter)
