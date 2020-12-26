import re

from typing import List, Set

rules = dict()
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

        rules[beginning] = [range(r[0], r[1] + 1) for r in split_ranges]


valid = set()
for rule_pair in rules.values():
  for rule in rule_pair:
    valid.update(rule)

valid_nearby_tickets = []
invalid_ns = []
for ticket in nearby_tickets:
  works = True

  for n in ticket:
    if n not in valid:
      invalid_ns.append(n)
      works = False
  
  if works:
    valid_nearby_tickets.append(ticket)
  

print('Part 1:', sum(invalid_ns))

possible_fields: List[Set[str]] = [set()] * len(your_ticket)
for ticket in valid_nearby_tickets:
  print(ticket)