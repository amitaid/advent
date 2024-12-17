package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Robot struct {
	Px, Py int
	Vx, Vy int
}

func main() {
	f, _ := os.ReadFile("24/day14/data.txt")
	x, y := 101, 103
	lines := strings.Split(string(f), "\n")
	var robots []*Robot
	for _, line := range lines {
		robots = append(robots, parseRobot(line))
	}
	// for _, robot := range robots {
	// 	fmt.Println(robot)
	// }
	// drawRobots(robots, y, x)
	// fmt.Println(calcScore(robots, y, x))

	for k := 1; k < 10000; k++ {

		for _, r := range robots {
			r.Px = (r.Px + r.Vx + 10000*x) % x
			r.Py = (r.Py + r.Vy + 10000*y) % y
		}
		board := getBoard(robots, y, x)
		justOnes := true
		for i := range board {
			for j := range board[i] {
				if board[i][j] > 1 {
					justOnes = false
				}
			}
		}
		if justOnes {
			drawRobots(robots, y, x)
			fmt.Println(k)
			fmt.Println("--------------------")
		}
	}
	// fmt.Println(calcScore(robots, y, x))
}

func parseRobot(raw string) *Robot {
	parts := strings.SplitN(raw, " ", 2)
	pos := strings.Split(parts[0][2:], ",")
	vel := strings.Split(parts[1][2:], ",")
	px, _ := strconv.Atoi(pos[0])
	py, _ := strconv.Atoi(pos[1])
	vx, _ := strconv.Atoi(vel[0])
	vy, _ := strconv.Atoi(vel[1])
	return &Robot{Px: px, Py: py, Vx: vx, Vy: vy}
}

func getBoard(robots []*Robot, y int, x int) [][]int {
	m := make([][]int, y)
	for i := range m {
		m[i] = make([]int, x)
	}
	for _, r := range robots {
		m[r.Py][r.Px] += 1
	}
	return m
}

func drawRobots(robots []*Robot, y int, x int) {
	m := getBoard(robots, y, x)
	sb := strings.Builder{}

	for i := range m {
		for _, n := range m[i] {
			if n == 0 {
				sb.WriteString(".")
			} else {
				sb.WriteByte(byte('0' + n))
			}
		}
		sb.WriteString("\n")
	}
	fmt.Println(sb.String())
}

func calcScore(robots []*Robot, y int, x int) int {
	quads := make([]int, 4)
	for _, r := range robots {
		if r.Py < y/2 && r.Px < x/2 {
			quads[0] += 1
		}
		if r.Py > y/2 && r.Px < x/2 {
			quads[1] += 1
		}
		if r.Py < y/2 && r.Px > x/2 {
			quads[2] += 1
		}
		if r.Py > y/2 && r.Px > x/2 {
			quads[3] += 1
		}
	}
	fmt.Println(quads)
	return quads[0] * quads[1] * quads[2] * quads[3]
}
