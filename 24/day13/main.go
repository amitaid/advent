package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

const regex = `Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)`

type Game struct {
	Ax int64
	Ay int64
	Bx int64
	By int64
	Tx int64
	Ty int64
}

func main() {
	p := regexp.MustCompile(regex)

	file, _ := os.ReadFile("24/day13/data.txt")
	matches := p.FindAllStringSubmatch(string(file), -1)

	var sum int64
	for _, match := range matches {
		ax, _ := strconv.ParseInt(match[1], 10, 64)
		ay, _ := strconv.ParseInt(match[2], 10, 64)
		bx, _ := strconv.ParseInt(match[3], 10, 64)
		by, _ := strconv.ParseInt(match[4], 10, 64)
		tx, _ := strconv.ParseInt(match[5], 10, 64)
		ty, _ := strconv.ParseInt(match[6], 10, 64)
		g := Game{Ax: ax, Ay: ay, Bx: bx, By: by, Tx: tx, Ty: ty}
		fmt.Println(g)

		a, b := getClose(g)
		a -= 500 // Give some leeway
		b -= 500

		g.Tx += extra - (a*g.Ax + b*g.Bx)
		g.Ty += extra - (a*g.Ay + b*g.By)

		fmt.Println()
		fmt.Println(g)
		r := game(g)
		if r < 10000 {
			sum += r + 3*a + b
		}
	}
	fmt.Println(sum)
}

func game(g Game) int64 {
	var cost int64 = 100000000000000000
	for b := range int64(10000) {
		for a := range int64(10000) {
			if a*g.Ax+b*g.Bx == g.Tx && a*g.Ay+b*g.By == g.Ty {
				cost = min(cost, 3*a+b)
			}
		}
	}
	return cost
}

const extra int64 = 10000000000000

func getClose(g Game) (int64, int64) {
	a := extra * (g.By - g.Bx) / (g.Ax*g.By - g.Ay*g.Bx)
	b := extra * (g.Ax - g.Ay) / (g.Ax*g.By - g.Ay*g.Bx)
	fmt.Println(a, b)
	return a, b
}
