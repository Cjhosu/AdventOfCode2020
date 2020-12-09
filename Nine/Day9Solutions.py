nums = []
target = 0
with open('Day9_input') as file: 
    for line in file:
        line = line.strip()
        nums.append(line)


class Validator:
    current_added = 0
    done = None

    def __init__(self, nums, idx):
        self.nums = nums
        self.idx = idx

    def checker(self):
        idx = self.idx
        self.current = nums[idx]
        self.checkset = nums[idx-25:idx]
        if not self.now_check(self.current, self.checkset):
            global target
            target = self.current
            print(self.current)
            return

    def now_check(self,current, checkset):
        for each in checkset:
            if str(int(current) - int(each)) in checkset:
                return True

    def adder(self, range_added):
        global target
        target = int(target)
        new_index = int(self.idx)  + 1
        if new_index == len(nums):
            return
        range_added.append(nums[self.idx])
        self.current_added += int(nums[self.idx])
        self.idx = new_index
        if self.current_added < target:
            self.adder(range_added)
        elif self.current_added > target:
            range_added = []
            self.current_added = 0
            return
        elif self.current_added == target and len(range_added) > 1:
            range_added.sort()
            print(range_added)
            self.done = True

for idx in range(25,len(nums)):
    v = Validator(nums, idx)
    v.checker()

for idx in range(0,len(nums)):
    v = Validator(nums, idx)
    if v.done != True:
        range_added = []
        v.adder(range_added)
    else:
        break
