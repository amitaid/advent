

def part1(filename):
  with open(filename) as f:
    equations = f.read().splitlines()
    val_cal = [e.split(': ') for e in equations]
    vc = [(int(p[0]), [int(x) for x in p[1].split(' ')]) for p in val_cal]
    
    res = 0
    for v in vc:
      if try_one(v[0], v[1]):
        res += v[0]

    print(res)
    
def try_one(result, nums, current = 0):
  if current == result:
    return True
  if current > result or not nums:
    return False
  
  head, tail = nums[0], nums[1:]
  if current == 0:
    return try_one(result, tail, head)

  return try_one(result, tail, current+head) or try_one(result, tail, current*head)

def try_conc(result, nums, current = 0):
  if current == result:
    return True
  if current > result or not nums:
    return False
  
  head, tail = nums[0], nums[1:]
  if current == 0:
    return try_conc(result, tail, head)

  return try_conc(result, tail, current+head) or try_conc(result, tail, current*head) or \
    try_conc(result, tail, int(str(current) + str(head)))

def part2(filename):
  with open(filename) as f:
    equations = f.read().splitlines()
    val_cal = [e.split(': ') for e in equations]
    vc = [(int(p[0]), [int(x) for x in p[1].split(' ')]) for p in val_cal]
    
    res = 0
    for v in vc:
      if try_conc(v[0], v[1]):
        res += v[0]

    print(res)

part2('24/day07/data.txt')
