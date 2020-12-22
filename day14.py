import re

from collections import defaultdict
from typing import List


with open('input/day14.txt') as f:
  program = [line.strip() for line in f.readlines()]


def apply_mask(mask: str, n: int) -> int:
  b = list(bin(n)[2:].zfill(36))

  for i in range(len(mask)):
    if mask[i] != 'X':
      b[i] = mask[i]

  return int(''.join(b), 2)


mem_p = re.compile(r'mem\[(\d+)] = (\d+)')
mem = defaultdict(lambda: 0)
mask = ''

for line in program:
  if line.startswith('mask'):
    mask = line.split('mask = ')[1]
  else:
    mem_m = mem_p.match(line)
    addr = int(mem_m.group(1))
    val = int(mem_m.group(2))

    mem[addr] = apply_mask(mask, val)

print('Part 1:', sum(mem.values()))


def apply_mask_part2(mask: str, n: int) -> str:
  b = list(bin(n)[2:].zfill(36))

  for i in range(len(mask)):
    if mask[i] != '0':
      b[i] = mask[i]

  return ''.join(b)


def all_possible(masked_addr: str) -> List[int]:
  num_x = masked_addr.count('X')
  ret = []

  for n in range(2 ** num_x):
    masked_addr_mutable = list(masked_addr)
    b = bin(n)[2:].zfill(num_x)
    b_idx = 0

    for i in range(len(masked_addr)):
      if masked_addr[i] == 'X':
        masked_addr_mutable[i] = b[b_idx]
        b_idx += 1
    
    ret.append(int(''.join(masked_addr_mutable), 2))
  
  return ret


mem = defaultdict(lambda: 0)
mask = ''

for line in program:
  if line.startswith('mask'):
    mask = line.split('mask = ')[1]
  else:
    mem_m = mem_p.match(line)
    masked_addr = apply_mask_part2(mask, int(mem_m.group(1)))

    for addr in all_possible(masked_addr):
      mem[addr] = int(mem_m.group(2))

print('Part 2:', sum(mem.values()))