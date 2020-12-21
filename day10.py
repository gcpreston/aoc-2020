from collections import defaultdict
from typing import List

with open('input/day10.txt') as f:
  adapters = sorted([int(n) for n in f.readlines()])

jolts = 0
diffs = defaultdict(int)

for n in adapters:
  diffs[n - jolts] += 1
  jolts = n
diffs[3] += 1

print('Part 1:', diffs[1] * diffs[3])


def num_compatible(source: int, adapters: List[int]) -> int:
  """
  Count the number of adapters that could fit in the source.
  Assumes adapter list is sorted.
  """
  count = 0
  for a in adapters:
    if a <= source + 3:
      count += 1
    else:
      break
  return count

d = dict()

def num_combos(source: int, adapters: List[int]) -> int:
  """ Assumes adapter list is sorted from lowest to highest. """
  l = len(adapters)

  if l in d:
    return d[l]
  if l == 0:
    return 1

  working = num_compatible(source, adapters)
  if working == 1:
    d[l] = num_combos(adapters[0], adapters[1:])
  elif working == 2:
    d[l] = num_combos(adapters[0], adapters[1:]) + num_combos(adapters[1], adapters[2:])
  elif working == 3:
    d[l] = num_combos(adapters[0], adapters[1:]) + num_combos(adapters[1], adapters[2:]) + num_combos(adapters[2], adapters[3:])

  return d[l]

print('Part 2:', num_combos(0, adapters))
