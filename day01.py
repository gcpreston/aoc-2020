from itertools import combinations

with open('input/day01.txt') as f:
  nums = [int(n) for n in f.read().strip().split('\n')]

# Part 1
for i in range(len(nums) - 1):
  for j in range(i + 1, len(nums)):
    if nums[i] + nums[j] == 2020:
      print(nums[i] * nums[j])

# Part 2
for triple in combinations(nums, 3):
  if sum(triple) == 2020:
    print(triple[0] * triple[1] * triple[2])


# Later solution:
# from functools import reduce

# def abstraction(collection, n):
#   for group in combinations(nums, n):
#     if sum(group) == 2020:
#       print(reduce(lambda x, y: x * y, group))

# abstraction(nums, 2)
# abstraction(nums, 3)