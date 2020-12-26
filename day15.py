from typing import Optional, List

with open('input/day15.txt') as f:
  starting_nums = [int(n) for n in f.read().strip().split(',')]


def last_time_spoken(nums: List[int], n: int) -> Optional[int]:
  """ Figure out the last time n appeared in nums. """
  i = len(nums) - 1
  for checking in reversed(nums):
    if checking == n:
      return i + 1
    i -= 1


def next_num(prev_nums: List[int]) -> int:
  last = prev_nums[-1]
  t0 = last_time_spoken(prev_nums[:-1], last)

  if not t0:
    return 0
  
  t1 = len(prev_nums)
  return t1 - t0


def turn_val(starting_nums: List[int], end_turn: int) -> int:
  turn = len(starting_nums) + 1
  mem = starting_nums.copy()

  while turn <= end_turn:
    mem.append(next_num(mem))
    turn += 1
  
  return mem[-1]


def turn_val_v2(starting_nums: List[int], end_turn: int) -> int:
  turn = len(starting_nums) + 1
  last_val = 0
  turn_last_seen = dict()
  seen = set(starting_nums)

  for i in range(len(starting_nums)):
    turn_last_seen[starting_nums[i]] = i + 1
    
  while turn < end_turn:
    if last_val not in seen:
      next_val = 0
    else:
      next_val = turn - turn_last_seen[last_val]

    seen.add(last_val)
    turn_last_seen[last_val] = turn
    last_val = next_val
    turn += 1
  
  return next_val


print('Part 1:', turn_val_v2(starting_nums, 2020))
print('Part 2:', turn_val_v2(starting_nums, 30000000))
