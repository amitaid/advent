package main

import (
	"bytes"
	"fmt"
	"os"
)

func dir(symbol byte) (int, int) {
	switch symbol {
	case '^':
		return -1, 0
	case 'v':
		return 1, 0
	case '>':
		return 0, 1
	case '<':
		return 0, -1
	default:
		return 0, 0
	}
}

func main() {
	part2("24/day15/data.txt")
}

func part1(filename string) {
	f, _ := os.ReadFile(filename)
	parts := bytes.SplitN(f, []byte{'\n', '\n'}, 2)
	m := bytes.Split(parts[0], []byte{'\n'})
	moves := bytes.ReplaceAll(parts[1], []byte{'\n'}, []byte{})

	cury, curx := findStart(m)

	printMap(m)
	for _, mov := range moves {
		cury, curx = move(m, mov, cury, curx)
	}
	printMap(m)
	fmt.Println(calcGps(m))
}

func findStart(m [][]byte) (int, int) {
	for i := range m {
		for j := range m[i] {
			if m[i][j] == '@' {
				return i, j
			}
		}
	}
	return -1, -1
}

func move(m [][]byte, move byte, cury int, curx int) (int, int) {
	diry, dirx := dir(move)
	y, x := cury+diry, curx+dirx

	if m[y][x] == '.' {
		m[y][x] = '@'
		m[cury][curx] = '.'
		return y, x
	}

	for m[y][x] != '.' {
		if m[y][x] == '#' {
			return cury, curx
		}
		y, x = y+diry, x+dirx
	}

	m[y][x] = 'O'
	m[cury][curx] = '.'
	m[cury+diry][curx+dirx] = '@'
	return cury + diry, curx + dirx
}

func printMap(m [][]byte) {
	fmt.Println(string(bytes.Join(m, []byte{'\n'})), "\n")
}

func calcGps(m [][]byte) int {
	score := 0
	for i := range m {
		for j := range m[i] {
			if m[i][j] == 'O' {
				score += 100*i + j
			}
		}
	}
	return score
}

func part2(filename string) {
	f, _ := os.ReadFile(filename)
	parts := bytes.SplitN(f, []byte{'\n', '\n'}, 2)
	m := bytes.Split(parts[0], []byte{'\n'})
	moves := bytes.ReplaceAll(parts[1], []byte{'\n'}, []byte{})
	m = widen(m)
	printMap(m)
	y, x := findStart(m)

	for _, mov := range moves {
		dy, dx := dir(mov)
		if canMoveBox(m, mov, y+dy, x+dx) {
			moveBox(m, mov, y+dy, x+dx)
			m[y][x] = '.'
			y += dy
			x += dx
			m[y][x] = '@'
		}
	}

	printMap(m)
	fmt.Println(calcGps2(m))
}

func widen(m [][]byte) [][]byte {
	res := make([][]byte, 0, len(m))
	for i := range len(m) {
		line := make([]byte, 0, 2*len(m[i]))
		for j := range len(m[i]) {
			if m[i][j] == 'O' {
				line = append(line, '[', ']')
			} else if m[i][j] == '@' {
				line = append(line, '@', '.')
			} else {
				line = append(line, m[i][j], m[i][j])
			}
		}
		res = append(res, line)
	}
	return res
}

func canMoveBox(m [][]byte, dir byte, y int, x int) bool {
	if x < 0 || y < 0 || y >= len(m)-1 || x >= len(m[y])-1 || m[y][x] == '#' {
		return false
	}
	if m[y][x] == '.' {
		return true
	}

	if m[y][x] == ']' {
		x -= 1
	}
	switch dir {
	case '^':
		if m[y-1][x] == '#' || m[y-1][x+1] == '#' {
			return false
		}
		if m[y-1][x] == '.' && m[y-1][x+1] == '.' {
			return true
		}
		return canMoveBox(m, dir, y-1, x) && canMoveBox(m, dir, y-1, x+1)
	case 'v':
		if m[y+1][x] == '#' || m[y+1][x+1] == '#' {
			return false
		}
		if m[y+1][x] == '.' && m[y+1][x+1] == '.' {
			return true
		}
		return canMoveBox(m, dir, y+1, x) && canMoveBox(m, dir, y+1, x+1)
	case '<':
		c := m[y][x-1]
		return c == '.' || c != '#' && canMoveBox(m, dir, y, x-1)
	case '>':
		c := m[y][x+2]
		return c == '.' || c != '#' && canMoveBox(m, dir, y, x+2)
	default:
		return false
	}
}

func moveBox(m [][]byte, dir byte, y int, x int) {
	if x < 0 || y < 0 || y >= len(m)-1 || x >= len(m[y])-1 || m[y][x] == '.' || m[y][x] == '#' {
		return
	}
	if m[y][x] == ']' {
		x -= 1
	}
	switch dir {
	case '^':
		moveBox(m, dir, y-1, x)
		moveBox(m, dir, y-1, x+1)
		m[y][x] = '.'
		m[y][x+1] = '.'
		m[y-1][x] = '['
		m[y-1][x+1] = ']'
	case 'v':
		moveBox(m, dir, y+1, x)
		moveBox(m, dir, y+1, x+1)
		m[y][x] = '.'
		m[y][x+1] = '.'
		m[y+1][x] = '['
		m[y+1][x+1] = ']'
	case '<':
		moveBox(m, dir, y, x-1)
		m[y][x-1] = '['
		m[y][x] = ']'
		m[y][x+1] = '.'
	case '>':
		moveBox(m, dir, y, x+2)
		m[y][x] = '.'
		m[y][x+1] = '['
		m[y][x+2] = ']'
	}
}

func calcGps2(m [][]byte) int {
	score := 0
	for i := range m {
		for j := range m[i] {
			if m[i][j] == '[' {
				score += 100*i + j
			}
		}
	}
	return score
}
