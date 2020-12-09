nums = []
target = None
with open('Day9_input') as file:
    for line in file:
        line = line.strip()
        nums.append(line)

def checker(idx):
     current = nums[idx]
     checkset = nums[idx-25:idx]
     if not now_check(current, checkset):
         global target
         target = current
         print(current)
         return

def now_check(current, checkset):
    for each in checkset:
        if str(int(current) - int(each)) in checkset:
            return True


for idx in range(25,len(nums)):
    checker(idx)

current_added = 0
range_added = []
done = None

def adder(idx):
    global range_added
    global current_added
    global target
    target = int(target)
    new_index = int(idx)  + 1
    range_added.append(nums[idx])
    current_added += int(nums[idx])
    if new_index == len(nums):
        return
    if current_added < target:
        adder(new_index)
    elif current_added > target:
        range_added = []
        current_added = 0
        adder(new_index)
    elif current_added == target and len(range_added) > 1:
        range_added.sort()
        print(range_added)
        global done
        done = True 

for idx in range(0,len(nums)):
    if done != True:
        adder(idx)
    else:
        break
