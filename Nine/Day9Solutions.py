nums = []
target = 0
with open('Day9_input') as file: 
    for line in file:
        line = line.strip()
        nums.append(int(line))


class Validator:
    done = None

    def __init__(self, nums, idx):
        self.nums = nums
        self.idx = idx

    def checker(self):
        idx = self.idx
        self.current = nums[idx]
        self.checkset = nums[idx-25:idx]
        if not self.now_check(self.current, self.checkset):
            print(self.current)
            global target
            target = self.current
            return

    def now_check(self,current, checkset):
        for each in checkset:
            if current - each in checkset:
                return True

    def adder(self, range_added, target):
        range_added.append(nums[self.idx])
        self.idx += 1
        summed_range = sum(range_added)
        if summed_range < target:
            self.adder(range_added, target)
        elif summed_range > target:
            range_added = []
            self.current_added = 0
            return
        elif summed_range == target and len(range_added) > 1:
            print(min(range_added) + max(range_added))
            self.done = True

for idx in range(25,len(nums)):
    v = Validator(nums, idx)
    v.checker()

for idx in range(0,len(nums)):
    v = Validator(nums, idx)
    if not v.done:
        range_added = []
        v.adder(range_added, target)
