from typing import Optional, List, Set, Tuple


def parse_line(line: str) -> Tuple[str, int]:
  l = line.strip().split(' ')
  l[1] = int(l[1])
  return tuple(l)


def run_instrs(instrs: List[Tuple[str, int]]) -> Optional[int]:
  acc = 0
  i = 0
  seen = set()

  while i < len(instrs):
    if i in seen:
      return None
    
    seen.add(i)
    inst, arg = instrs[i]
    if inst == 'jmp':
      i += int(arg)
    else:
      i += 1
    if inst == 'acc':
      acc += int(arg)
  
  return acc


def has_loop(instrs: List[Tuple[str, int]]) -> bool:
  pass

with open('input/day08.txt') as f:
  instrs = [parse_line(line) for line in f.readlines()]

for i in range(len(instrs)):
  if instrs[i][0] == 'jmp':
    test_instrs = instrs.copy()
    test_instrs[i] = ('nop', 0)
    v = run_instrs(test_instrs)

    if v is not None:
      print(v)

print('Finished, did anything happen?')

# OLD CRAP
# acc = 0
# i = 0
# prev = None
# ran = set()

# last_jmp = 0
# while i < len(instrs):
#   if instrs[i][0] == 'jmp':
#     last_jmp = i
#   i += 1

# fixed_instrs[last_jmp] = ('nop', '+0')

# while i < len(instrs):
#   if i in ran:
#     break

#   prev = i
#   ran.add(i)
#   inst, arg = instrs[i]

#   if inst == 'acc':
#     acc += int(arg)
#     i += 1
#   elif inst == 'jmp':
#     i += int(arg)
#   else:
#     i += 1
  
#   if i in ran:
#     print('fixed', prev, instrs[prev])
#     fixed_instrs[prev] = ('nop', '+0')


# for instr in fixed_instrs:
#   print(*instr)

# i = 0
# while i < len(fixed_instrs):
#   inst, arg = fixed_instrs[i]

#   if inst == 'acc':
#     acc += int(arg)
#     i += 1
#   elif inst == 'jmp':
#     i += int(arg)
#   else:
#     i += 1

# print(acc)