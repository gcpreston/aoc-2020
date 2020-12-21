from typing import List, Tuple

with open('input/day12.txt') as f:
  directions = f.readlines()


def handle_letter(p: Tuple[int, int], facing: int, letter: str, num: int) -> Tuple[Tuple[int, int], int]:
  new_p = p
  deg_to_dir = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}

  if letter == 'N':
    new_p = (p[0], p[1] + num)
  elif letter == 'S':
    new_p = (p[0], p[1] - num)
  elif letter == 'E':
    new_p = (p[0] + num, p[1])
  elif letter == 'W':
    new_p = (p[0] - num, p[1])
  elif letter == 'L':
    facing += num
  elif letter == 'R':
    facing -= num
  elif letter == 'F':
    new_letter = deg_to_dir[facing % 360]
    return handle_letter(p, facing, new_letter, num)
  
  return new_p, facing


def follow_directions(directions: List[str]) -> Tuple[int, int]:
  p = (0, 0)  # x, y
  facing = 0  # direction in degrees

  for d in directions:
    letter = d[0]
    num = int(d[1:])
    p, facing = handle_letter(p, facing, letter, num)

  return p, facing


end, facing = follow_directions(directions)
print('Part 1:', abs(end[0]) + abs(end[1]))


def handle_letter_part2(p: Tuple[int, int], waypoint: Tuple[int, int], letter: str, num: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
  new_p = p
  new_waypoint = waypoint
  deg_to_dir = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}

  if letter == 'N':
    new_waypoint = (waypoint[0], waypoint[1] + num)
  elif letter == 'S':
    new_waypoint = (waypoint[0], waypoint[1] - num)
  elif letter == 'E':
    new_waypoint = (waypoint[0] + num, waypoint[1])
  elif letter == 'W':
    new_waypoint = (waypoint[0] - num, waypoint[1])
  elif letter == 'L':
    if num == 90:
      new_waypoint = (-1 * waypoint[1], waypoint[0])
    elif num == 180:
      new_waypoint = (-1 * waypoint[0], -1 * waypoint[1])
    elif num == 270:
      new_waypoint = (waypoint[1], -1 * waypoint[0])
    else:
      new_waypoint = waypoint
  elif letter == 'R':
    if num == 90:
      new_waypoint = (waypoint[1], -1 * waypoint[0])
    elif num == 180:
      new_waypoint = (-1 * waypoint[0], -1 * waypoint[1])
    elif num == 270:
      new_waypoint = (-1 * waypoint[1], waypoint[0])
    else:
      new_waypoint = waypoint
  elif letter == 'F':
    for _ in range(num):
      new_p = (new_p[0] + waypoint[0], new_p[1] + waypoint[1])
  
  return new_p, new_waypoint



def follow_directions_part2(directions: List[str]) -> Tuple[int, int]:
  p = (0, 0)  # x, y
  waypoint = (10, 1)

  for d in directions:
    letter = d[0]
    num = int(d[1:])
    p, waypoint = handle_letter_part2(p, waypoint, letter, num)

  return p, waypoint


end, end_point = follow_directions_part2(directions)
print('Part 2:', abs(end[0]) + abs(end[1]))
