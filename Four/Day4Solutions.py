valid_passports = 0
class Passport:
    valid_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    def __init__(self, docs):
        self.docs = docs

    def make_passport(self):
        pass_doc = {}
        for i in self.docs:
            k,v = i.split(':')
            pass_doc[k] = v
        self.pass_doc = pass_doc

    def validate(self):
        if all (elem in self.pass_doc for elem in self.valid_fields):
            self.check_data(self.pass_doc)

    def check_data(self, pass_doc):

        if not self.eye_color(pass_doc):
            return

        if not self.birth_year(pass_doc):
            return

        if not self.issue_year(pass_doc):
            return

        if not self.exp_year(pass_doc):
            return

        if not self.pass_id(pass_doc):
            return

        if not self.height(pass_doc):
            return

        if not self.hair_color(pass_doc):
            return

        global valid_passports
        valid_passports += 1

    def eye_color(self, pass_doc):
        if pass_doc['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
            return True

    def birth_year(self, pass_doc):
        birth_year = int(pass_doc['byr'])
        if birth_year >= 1920 and birth_year <= 2002:
            return True

    def issue_year(self, pass_doc):
        issue_year = int(pass_doc['iyr'])
        if issue_year >= 2010 and  issue_year <= 2020:
            return True

    def exp_year(self, pass_doc):
        exp_year= int(pass_doc['eyr']) 
        if exp_year >= 2020 and exp_year <= 2030:
            return True

    def pass_id(self, pass_doc):
        if len(pass_doc['pid']) == 9:
            return True

    def height(self, pass_doc):
        ht = pass_doc['hgt']
        unit = ht[-2:]
        val = int(ht[:-2])
        if (unit == 'cm' and val >= 150 and val <= 193) or (unit =='in'and val >= 59 and val<= 76):
            return True

    def hair_color(self, pass_doc):
        colo = pass_doc['hcl']
        if len(colo) == 7 and colo[0] == '#':
            return True

with open('Day4_input') as file:
    docs = []
    for line in file:
        if line != '\n':
            line = line.strip()
            elem = line.split(' ')
            for each in elem:
                docs.append(each)
        else:
            p = Passport(docs)
            p.make_passport()
            p.validate()
            docs = []
    else:
        p = Passport(docs)
        p.make_passport()
        p.validate()
        docs = []

print(valid_passports)
