with open('input/day09.txt') as f:
  nums = [int(n) for n in f.readlines()]


def valid(preamble, n) -> bool:
  for i in range(len(preamble) - 1):
    for j in range(i, len(preamble)):
      if i != j:
        if preamble[i] + preamble[j] == n:
          return True
  return False

preamble_len = 25
preamble = nums[:preamble_len]
i = preamble_len
n = nums[i]
while i < len(nums):
  if not valid(preamble, n):
    break

  preamble.pop(0)
  preamble.append(n)
  i += 1
  n = nums[i]

part1_ans = n
print('Part 1:', part1_ans)


def encryption_weakness(nums: list, invalid: int) -> int:
  begin = 0
  end = 1
  while begin < len(nums):
    if end < len(nums):
      s = nums[begin:end]

      if sum(s) == invalid:
        return min(s) + max(s)
      elif sum(s) > invalid:
        begin += 1
        end = begin + 1
      else:
        end += 1
    else:
      begin += 1
      end = begin + 1


print('Part 2:', encryption_weakness(nums, part1_ans))
