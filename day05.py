from typing import Tuple

with open('input/day05.txt') as f:
  passes = [line.strip() for line in f.readlines()]


def position(seat: str) -> Tuple[int, int]:
  """ Get (row, col) of seat (length 10) """
  row_range = [0, 128]
  col_range = [0, 8]

  for i in range(len(seat)):
    if i < 7:
      if seat[i] == 'F':
        row_range[1] -= (row_range[1] - row_range[0]) / 2
      else:
        row_range[0] += (row_range[1] - row_range[0]) / 2
    
    else:
      if seat[i] == 'L':
        col_range[1] -= (col_range[1] - col_range[0]) / 2
      else:
        col_range[0] += (col_range[1] - col_range[0]) / 2
  
  return int(row_range[0]), int(col_range[0])


def seat_id(pos: Tuple[int, int]) -> int:
  return (pos[0] * 8) + pos[1]

print('Part 1:', max([seat_id(position(seat)) for seat in passes]))

prev = 12
for n in sorted([seat_id(position(seat)) for seat in passes]):
  if n != prev + 1:
    print('Part 2:', prev + 1)
  prev = n