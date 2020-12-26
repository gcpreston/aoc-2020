with open('input/day23_test.txt') as f:
  cups = [int(n) for n in f.read().strip()]


def cups_str(cups, selected=None):
  s = ''
  for c in cups:
    if selected and c == selected:
      s += f'({c}) '
    else:
      s += f'{c} '
  return s[:-1]


def move(cups: list, selected: int) -> list:
  idx = cups.index(selected)
  pickup = cups[idx + 1 : idx + 4]
  stay = cups[:idx + 1] + cups[idx + 4:]
  if idx + 4 >= len(cups):
    remainder = len(cups) - (idx + 1)
    pickup += cups[:3 - remainder]
    stay = stay[3 - remainder:]

  remaining_smaller = [s for s in stay if s < selected]
  destination = max(remaining_smaller) if remaining_smaller else max(stay)

  dst_idx = stay.index(destination)
  # print(f'{cups_str(cups, selected)} pickup {cups_str(pickup)} stay {cups_str(stay, selected)} destination {destination}')
  cups = stay[:dst_idx + 1] + pickup + stay[dst_idx + 1:]
  return cups


def run(cups: list, moves: int) -> str:
  i = 1
  selected = cups[0]
  while i <= moves:
    cups = move(cups, selected)
    selected = cups[(cups.index(selected) + 1) % len(cups)]
    i += 1
  
  return ''.join([str(n) for n in cups[cups.index(1) + 1:] + cups[:cups.index(1)]])


# Something's broken but whatever I'm rewriting this anyways
# print('Part 1:', run(cups, 2020))


class Node:
  val: int = 0
  next: 'Node' = None

  def __init__(self, val = None):
    self.val = val

lookup = dict()
head = Node()
last = head
max_val = None

with open('input/day23.txt') as f:
  contents = f.read()

max_val = max([int(n) for n in contents])
head.val = int(contents[0])
lookup[head.val] = head

for s in contents[1:]:
  n = Node(int(s))
  lookup[n.val] = n
  last.next = n
  last = n

for i in range(max_val + 1, 1000001):
  n = Node(i)
  lookup[n.val] = n
  last.next = n
  last = n

max_val = 1000000
last.next = head
print('lookup size:', len(lookup))

def move_v2(cur: Node, max_val: int) -> Node:
  pickup = cur.next

  # Take 3 out of chain
  cur.next = cur.next.next.next.next

  pickup_vals = [pickup.val, pickup.next.val, pickup.next.next.val]
  
  test = cur.val - 1 if cur.val - 1 != 0 else max_val
  while test in pickup_vals:
    test = test - 1
    if test == 0:
      test = max_val
  dest = test
  
  # print('cur.val:', cur.val)
  # print('pickup:', pickup_vals)
  # print('dest:', dest)

  dest_node = lookup[dest]
  
  temp = dest_node.next
  dest_node.next = pickup
  pickup.next.next.next = temp

  return cur.next


moves = 1
cur = head
while moves <= 10000000:
  # print('move:', moves)
  cur = move_v2(cur, max_val)
  moves += 1
  # print()

# Part 1 stuff
# cur = lookup[1]

# cur = cur.next
# answer = ''
# while cur.val != 1:
#   answer += str(cur.val)
#   cur = cur.next
# print('Part 1:', answer)

cur = lookup[1]

print(cur.next.val, cur.next.next.val)
print('Part 2:', cur.next.val * cur.next.next.val)
