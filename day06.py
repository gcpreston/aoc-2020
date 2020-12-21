with open('input/day06.txt') as f:
  contents = [[person for person in group.split('\n')] for group in f.read().split('\n\n')]


def count_answers(group: list) -> int:
  seen = set()
  for person in group:
    for q in person:
      seen.add(q)
  return len(seen)

print('Part 1:', sum(map(count_answers, contents)))


def count_answers2(group: list) -> int:
  valid = set(group[0])

  for person in group:
    letters = set(person)
    new_valid = set()

    for q in valid:
      if q in letters:
        new_valid.add(q)
    
    valid = new_valid

  return len(valid)

print('Part 2:', sum(map(count_answers2, contents)))
