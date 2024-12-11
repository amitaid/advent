
import math


v = {
  '^': -1,
  '>': 0,
  'v': 1,
  '<': 2,
}

def next(y, x, dir, maze):
  ny, nx = y + int(math.floor(math.sin(dir*math.pi/2)+0.5)), x + int(math.floor(math.cos(dir*math.pi/2)+0.5))
  odir = dir
  while in_maze(ny, nx, maze) and maze[ny][nx] == '#':
    dir += 1
    if dir == odir:
      print('error looping')
      return -1, -1, -1
    
    ny, nx = y + int(math.floor(math.sin(dir*math.pi/2)+0.5)), x + int(math.floor(math.cos(dir*math.pi/2)+0.5))

  return ny, nx, dir % 4

def print_maze(maze):
  print('\n')
  for m in maze:
    print(m)

def in_maze(y, x, maze):
  return y >= 0 and y < len(maze) and x >= 0 and x < len(maze[y])

def part1(filename):
  with open(filename) as f:
    maze = f.read().splitlines()
    dir = 0
    x, y = -1, -1

    for i in range(len(maze)):
      for j in range(len(maze[i])):
        if maze[i][j] in '^><v':
          dir = v[maze[i][j]]
          y, x = i, j
          break
    
    count = 0
    while True:
      if not in_maze(y, x, maze):
        print_maze(maze)
        print(count)
        return
      
      ny, nx, dir = next(y, x, dir, maze)

      if maze[y][x] != 'X':
        count += 1
        maze[y] = maze[y][:x] + 'X' + maze[y][x+1:]
      y, x = ny, nx
    


def test_loop(y, x, dir, maze):
  seen = {(y,x, dir)}
  a, b, newdir = next(y, x, dir, maze)
  if newdir != dir:
    dir += 1
  dir += 1
  while in_maze(y, x, maze):
    y, x, dir = next(y, x, dir, maze)
    if (y, x, dir) in seen:
      return (y, x, dir)
    else:
      seen.add((y, x, dir))

  return None

def part2(filename):
  with open(filename) as f:
    maze = f.read().splitlines()
    dir = 0
    x, y = -1, -1

    for i in range(len(maze)):
      for j in range(len(maze[i])):
        if maze[i][j] in '^><v':
          dir = v[maze[i][j]]
          y, x = i, j
          break
    
    count = 0
    loops = 0
    starty, startx = y, x
    while True:
      if not in_maze(y, x, maze):
        # print_maze(maze)
        print(count)
        print(loops)
        return
      
      if y != starty and x != startx:
        loop = test_loop(y, x, dir, maze)
        if loop:
          loops += 1
      
      ny, nx, dir = next(y, x, dir, maze)

      if maze[y][x] != 'X':
        count += 1
        maze[y] = maze[y][:x] + 'X' + maze[y][x+1:]
      y, x = ny, nx

part2("24/day06/data.txt")
