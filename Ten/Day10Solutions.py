nums = []
with open('Day10_sample') as file: 
    for line in file:
        line = line.strip()
        nums.append(int(line))

nums.append(0)
nums.append(max(nums) + 3)
nums.sort()


print(nums)
intervals = []

def track_adapter_steps(nums, start):
    for each in nums:
        intervals.append(each - start)
        start = each

    print(intervals)
    print(intervals.count(1))
    print(intervals.count(3))

track_adapter_steps(nums, 0)

from collections import defaultdict 

paths = defaultdict(int)
#paths = {}
adapters = nums
paths[0] = 1
print(paths)

for adapter in sorted(adapters):
    for diff in range(1, 4):
        next_adapter = adapter + diff
        if next_adapter in adapters:
            paths[next_adapter] += paths[adapter]
            print(paths)
