import math

from typing import List, Tuple

with open('input/day13.txt') as f:
  t, busses = f.readlines()

t = int(t)
busses = [int(b) if b != 'x' else b for b in busses.split(',')]

best_bus = None
best_time = math.inf
for b in busses:
  if b != 'x':
    wait = b - (t % b)
    if wait < best_time:
      best_bus = b
      best_time = wait

print('Part 1:', best_bus * best_time)

constraints = []
for i in range(len(busses)):
  if busses[i] != 'x':
    print(f'constraint: x + {i} % {busses[i]} == 0')
    constraints.append((i, busses[i]))

def check_constraint(c: Tuple[int, int], x: int):
  return (x + c[0]) % c[1] == 0

def lcm(nums: List[int]) -> int:
  l = nums[0]
  for i in nums[1:]:
    l = l * i // math.gcd(l, i)
  return l

bus_ids = [b for b in busses if b != 'x']
upper_limit = lcm(bus_ids)
print('Upper limit:', upper_limit)

checking = 0
idx = 0
increment_by = 1

while idx < len(bus_ids):
  checking += increment_by

  if check_constraint(constraints[idx], checking):
    increment_by = lcm([increment_by, bus_ids[idx]])
    idx += 1
  
  if checking > upper_limit:
    print('Upper limit reached, whoops ;-; idx:', idx)
    break
    
print('Part 2:', checking)
