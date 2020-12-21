import re

with open('input/day04.txt') as f:
  data = [{k: v for k, v in [field.split(':') for field in re.split(' |\n', passport) if field]} for passport in f.read().split('\n\n')]

def all_in(items, d) -> bool:
  """ Check if every item is contained in collection d """
  for i in items:
    if i not in d:
      return False
  return True

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

count = 0
for d in data:
  if all_in(required, d):
    count += 1

print('Part 1:', count)


def check_byr(val):
  return 1920 <= int(val) <= 2002

def check_iyr(val):
  return 2010 <= int(val) <= 2020

def check_eyr(val):
  return 2020 <= int(val) <= 2030

def check_hgt(val):
  if val.endswith('cm'):
    return 150 <= int(val[:-2]) <= 193
  else:
    return 59 <= int(val[:-2]) <= 76

def check_hcl(val):
  p = re.compile(r'#[0-9a-f]{6}')
  return p.match(val)

def check_ecl(val):
  return val in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def check_pid(val):
  return len(val) == 9

def check_cid(val):
  return True

checks = {
  'byr': check_byr,
  'iyr': check_iyr,
  'eyr': check_eyr,
  'hgt': check_hgt,
  'hcl': check_hcl,
  'ecl': check_ecl,
  'pid': check_pid,
  'cid': check_cid
}

def constraints_pass(d) -> bool:
  """ Check if each constraint passes for a passport """
  for k, v in d.items():
    if not checks[k](v):
      return False
  return True

count2 = 0
for d in data:
  if all_in(required, d) and constraints_pass(d):
    count2 += 1

print('Part 2:', count2)