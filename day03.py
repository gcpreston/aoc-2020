from typing import Tuple

with open('input/day03.txt') as f:
  contents = [line.strip() for line in f.readlines()]

width = len(contents[0])
end = len(contents)


def move(pos: Tuple[int, int], d: Tuple[int, int]) -> Tuple[int, int]:
  return (pos[0] + d[0], (pos[1] + d[1]) % width)


def simulate(r, c) -> int:
  pos = (0, 0)  # row, col
  trees = 0

  while pos[0] < end:
    if contents[pos[0]][pos[1]] == '#':
      trees += 1
    
    pos = move(pos, (r, c))

  return trees


print('Part 1:', simulate(1, 3))
print('Part 2:', simulate(1, 1) * simulate(1, 3) * simulate(1, 5) * simulate(1, 7) * simulate(2, 1))
