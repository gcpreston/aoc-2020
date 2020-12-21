import copy

from typing import List, Tuple


with open('input/day11.txt') as f:
  seats = [list(line.strip()) for line in f.readlines()]


def count_adj(seats: List[List[str]], row: int, col: int) -> int:
  adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  count = 0

  for a in adj:
    check_row = row + a[0]
    check_col = col + a[1]
    if 0 <= check_row < len(seats) and 0 <= check_col < len(seats[check_row]):
      c = seats[row + a[0]][col + a[1]]
      if c == '#':
        count += 1
  
  return count


def count_adj_part2(seats: List[List[str]], row: int, col: int) -> int:
  adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  count = 0

  for a in adj:
    if occupied_in_direction(seats, row, col, a):
      count += 1
  
  return count


def occupied_in_direction(seats: List[List[str]], row: int, col: int, direction: Tuple[int, int]) -> bool:
  check_row = row + direction[0]
  check_col = col + direction[1]

  while 0 <= check_row < len(seats) and 0 <= check_col < len(seats[check_row]):
    if seats[check_row][check_col] != '.':
      return seats[check_row][check_col] == '#'

    check_row += direction[0]
    check_col += direction[1]
  
  return False


def run_round(seats: List[List[str]], part2: bool) -> Tuple[List[List[str]], int]:
  new_seats = copy.deepcopy(seats)  # probably don't need to do this
  count = 0

  count_func = count_adj_part2 if part2 else count_adj
  tolerance = 5 if part2 else 4

  for r in range(len(seats)):
    for c in range(len(seats[r])):
      if seats[r][c] == '#' and count_func(seats, r, c) >= tolerance:
        new_seats[r][c] = 'L'
      elif seats[r][c] == 'L' and count_func(seats, r, c) == 0:
        new_seats[r][c] = '#'
      
      if new_seats[r][c] == '#':
        count += 1
  
  return new_seats, count


def print_seats(seats: List[List[str]]) -> None:
  for row in seats:
    print(''.join(row))

# print(count_adj_part2(seats, 3, 3))
# import sys
# sys.exit(0)


prev_count = -1
count = 0
while count != prev_count:
  prev_count = count
  seats, count = run_round(seats, False)

print('Part 1:', count)

with open('input/day11.txt') as f:
  seats = [list(line.strip()) for line in f.readlines()]

prev_count = -1
count = 0
while count != prev_count:
  prev_count = count
  seats, count = run_round(seats, True)

print('Part 2:', count)