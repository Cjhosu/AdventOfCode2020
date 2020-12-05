valid_passports = 0
class Passport:
    valid_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    def __init__(self, docs):
        test_fields = []
        for i in docs:
            k,v = i.split(':')
            test_fields.append(k)
        if all(elem in test_fields for elem in self.valid_fields):
            global valid_passports
            valid_passports += 1

with open('Day4_input') as file:
    docs = []
    for line in file:
        if line != '\n':
            line = line.strip()
            elem = line.split(' ')
            for each in elem:
                docs.append(each)
        else:
            Passport(docs)
            docs = []
    else:
        Passport(docs)
        docs = []

print(valid_passports)



