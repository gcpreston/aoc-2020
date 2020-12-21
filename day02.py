from typing import Tuple

with open('input/day02.txt') as f:
  data = [line.strip().split(': ') for line in f.readlines()]


def parse_policy(policy: str) -> Tuple[int, int, str]:
  r, letter = policy.split(' ')
  a, b = (int(n) for n in r.split('-'))
  return a, b, letter


def check_policy(policy: str, password: str) -> bool:
  smallest, largest, letter = parse_policy(policy)
  return smallest <= password.count(letter) <= largest


def check_policy2(policy: str, password: str) -> bool:
  a, b, letter = parse_policy(policy)
  return (password[a - 1] == letter) != (password[b - 1] == letter)

print('Part 1:', sum(map(lambda d: check_policy(*d), data)))
print('Part 2:', sum(map(lambda d: check_policy2(*d), data)))