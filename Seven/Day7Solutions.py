import re

with open('Day7_sample') as file:
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
        if full[k].has_key(colo):
            recurlist.append(k)
            recur(k)

recur('shiny gold')
recurset = set((recurlist))
print(recurset)
print(len(recurset))

def recurcount(colo):
    for k in full:
        if k == colo:
            print full[k]
            these = full[k].values()
            for each in these:
                print(each)
            for those in full[k].keys():
                recurcount(those)


recurcount('shiny gold')
