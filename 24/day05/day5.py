

from collections import defaultdict


def part1(filename):
  with open(filename) as f:
    rules = list()
    rule = f.readline()[:-1]
    while rule:
      [before, after] = rule.split('|')
      rules += [(before, after)]
      rule = f.readline()[:-1]
    
    res = 0
    pages = f.readline()[:-1]
    while pages:
      order = defaultdict(lambda: -1)
      split = pages.split(',')
      for i in range(len(split)):
        order[split[i]] = i
      
      badrules = list()
      for rule in rules:
        if order[rule[0]] != -1 and order[rule[1]] != -1 and order[rule[0]] > order[rule[1]]:
          badrules += [rule] 
      if not badrules:
        res += int(split[len(split)/2])
      pages = f.readline()[:-1]

    print(res)

def part2(filename):
  with open(filename) as f:
    rules = list()
    rule = f.readline()[:-1]
    while rule:
      [before, after] = rule.split('|')
      rules += [(before, after)]
      rule = f.readline()[:-1]
    
    res = 0
    pages = f.readline()[:-1]
    while pages:
      order = defaultdict(lambda: -1)
      split = pages.split(',')
      for i in range(len(split)):
        order[split[i]] = i
      
      badrules = list()
      for rule in rules:
        if order[rule[0]] != -1 and order[rule[1]] != -1 and order[rule[0]] > order[rule[1]]:
          badrules += [rule]
          continue
      if badrules:  #incorrect order
        pages_before = defaultdict(lambda: 0) # building correct order by finding how many pages are before
        for rule in rules:
          if order[rule[0]] != -1 and order[rule[1]] != -1:
            pages_before[rule[1]] += 1
            pages_before[rule[0]] = pages_before[rule[0]]
        s = [k for k in pages_before]
        s.sort(key=lambda p: pages_before[p])
        res += int(s[len(split)/2])
        print(s[len(split)/2])
      pages = f.readline()[:-1]

    print(res)
    

part2('24/day05/data.txt')