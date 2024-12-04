
def part1(): # 479
  with open('24/day02/data.txt') as f:
    report = f.readline()
    res = 0
    while report:
      if same_dir([int(num) for num in report.split()]):
        res += 1
      report = f.readline()
    print(res)

def same_dir(l):
  dir = [l[i]-l[i+1] for i in range(len(l)-1)]
  return all(x != 0 and dir[0]*x > 0 and abs(x) <= 3 for x in dir)

def part2():
  with open('24/day02/data.txt') as f:
    report = f.readline()
    res = 0
    while report:
      l = [int(num) for num in report.split()]
      if same_dir(l) or any(same_dir(l[:i]+l[i+1:]) for i in range(len(l))):
        res += 1
      
      report = f.readline()
    print(res)

part2()