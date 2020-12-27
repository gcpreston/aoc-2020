import re

from typing import Optional, List, Set, Tuple, Dict

rules = dict()  # name: (range, range)
your_ticket = None
nearby_tickets = []

with open('input/day16.txt') as f:
  yours = False
  nearby = False

  for line in f.readlines():
    stripped = line.strip()

    if yours:
      your_ticket = [int(n) for n in stripped.split(',')]
      yours = False
    elif nearby:
      nearby_tickets.append([int(n) for n in stripped.split(',')])
    else:
      if stripped == 'your ticket:':
        yours = True
      elif stripped == 'nearby tickets:':
        nearby = True
      elif stripped:
        beginning = stripped[:stripped.index(':')]
        end = stripped[stripped.index(':') + 2:]
        ranges = end.split(' or ')
        split_ranges = [[int(n) for n in r.split('-')] for r in ranges]

        parsed_ranges = tuple(range(r[0], r[1] + 1) for r in split_ranges)
        rules[beginning] = parsed_ranges


valid = set()
for rule_pair in rules.values():
  for rule in rule_pair:
    valid.update(rule)

valid_tickets = [your_ticket]
invalid_ns = []
for ticket in nearby_tickets:
  works = True

  for n in ticket:
    if n not in valid:
      invalid_ns.append(n)
      works = False
  
  if works:
    valid_tickets.append(ticket)

print('Part 1:', sum(invalid_ns))


class FigureOuter:
  possible_fields: List[Set[str]] = []

  def __init__(self, field_count: int, rule_names):
    for _ in range(field_count):
      self.possible_fields.append(set(rule_names))

  @property
  def taken_fields(self) -> List[Optional[str]]:
    return [next(iter(s)) if len(s) == 1 else None for s in self.possible_fields]
  
  @staticmethod
  def range_contains(rule: Tuple[range, range], n: int) -> bool:
    return n in rule[0] or n in rule[1]
  
  def figure_out(self, rules: Dict[str, Tuple[range, range]], tickets: List[List[int]]) -> None:
    i = 0
    while None in self.taken_fields:
      # import pdb
      # pdb.set_trace()
      ticket = tickets[i]

      # j is index we are figuring something out for
      for j in range(len(ticket)):
        to_remove: Set[str] = set()

        for name in self.possible_fields[j]:
          if not FigureOuter.range_contains(rules[name], ticket[j]):
            to_remove.add(name)
          if name in self.taken_fields and self.taken_fields.index(name) != j:
            to_remove.add(name)
        
        self.possible_fields[j] = self.possible_fields[j].difference(to_remove)
      
      i = (i + 1) % len(tickets)

  
fo = FigureOuter(len(your_ticket), rules.keys())
fo.figure_out(rules, valid_tickets)

part2_ans = 1
for i in range(len(fo.taken_fields)):
  if fo.taken_fields[i].startswith('departure'):
    part2_ans *= your_ticket[i]

print('Part 2:', part2_ans)
