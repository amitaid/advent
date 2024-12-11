
from collections import defaultdict

def in_range(node, y, x):
  return node[0]>=0 and node[0]<y and node[1]>=0 and node[1]<x

def part1(filename):
  with open(filename) as f:
    m = f.read().splitlines()
    y = len(m)
    x = len(m[0])
    ant_by_let = defaultdict(lambda: list())

    for i in range(y):
      for j in range(x):
        if m[i][j] != '.':
          ant_by_let[m[i][j]] = ant_by_let[m[i][j]] + [(i,j)]
    
    nodes = set()
    for t in ant_by_let:
      for a in ant_by_let[t]:
        for b in ant_by_let[t]:
          if a != b:
            diffy = a[0]-b[0]
            diffx = a[1]-b[1]
            if in_range((a[0]+diffy, a[1]+diffx), y, x):
              nodes.add((a[0]+diffy, a[1]+diffx))
            if in_range((b[0]-diffy, b[1]-diffx), y, x):
              nodes.add((b[0]-diffy, b[1]-diffx))
      
    print(len(nodes))

    for n in nodes:
      m[n[0]] = m[n[0]][:n[1]]+'#'+m[n[0]][n[1]+1:]

    for l in m:
      print(l)


def part2(filename):
  with open(filename) as f:
    m = f.read().splitlines()
    y = len(m)
    x = len(m[0])
    ant_by_let = defaultdict(lambda: list())

    for i in range(y):
      for j in range(x):
        if m[i][j] != '.':
          ant_by_let[m[i][j]] = ant_by_let[m[i][j]] + [(i,j)]
    
    nodes = set()
    for t in ant_by_let:
      for a in ant_by_let[t]:
        for b in ant_by_let[t]:
          if a != b:
            diffy = a[0]-b[0]
            diffx = a[1]-b[1]

            n = a
            while in_range(n, y, x):
              nodes.add(n)
              n = (n[0]+diffy, n[1]+diffx)
            n = b
            while in_range(n, y, x):
              nodes.add(n)
              n = (n[0]-diffy, n[1]-diffx)
      
    print(len(nodes))

    for n in nodes:
      m[n[0]] = m[n[0]][:n[1]]+'#'+m[n[0]][n[1]+1:]

    for l in m:
      print(l)

part2('24/day08/data.txt')