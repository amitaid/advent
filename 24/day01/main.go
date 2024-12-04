package main

import (
	"bytes"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	part2("24/day01/data.txt")

}

func part2(filename string) {
	data, _ := os.ReadFile(filename)
	lines := bytes.Split(data, []byte{'\n'})
	var l1 []int
	occ := make(map[int]int)
	for _, line := range lines {
		parts := bytes.Split(line, []byte{' ', ' ', ' '})
		n1, _ := strconv.ParseInt(string(parts[0]), 10, 32)
		l1 = append(l1, int(n1))
		n2, _ := strconv.ParseInt(string(parts[1]), 10, 32)
		n := int(n2)
		if _, exist := occ[n]; !exist {
			occ[n] = 0
		}
		occ[n] = occ[n] + 1
	}
	sort.Ints(l1)

	sum := 0
	for _, num := range l1 {
		d := num * occ[num]
		sum += d
	}
	fmt.Println(sum)
}

func part1(filename string) {
	data, _ := os.ReadFile(filename)
	lines := bytes.Split(data, []byte{'\n'})
	var l1, l2 []int
	for _, line := range lines {
		parts := bytes.Split(line, []byte{' ', ' ', ' '})
		n1, _ := strconv.ParseInt(string(parts[0]), 10, 64)
		l1 = append(l1, int(n1))
		n2, _ := strconv.ParseInt(string(parts[1]), 10, 64)
		l2 = append(l2, int(n2))
	}
	sort.Ints(l1)
	sort.Ints(l2)

	sum := 0
	for i := range l1 {
		d := l1[i] - l2[i]
		if d < 0 {
			d *= -1
		}
		sum += d
	}
	fmt.Println(sum)
}
