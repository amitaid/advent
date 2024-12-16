package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

const ex = "125 17"
const data = "1750884 193 866395 7 1158 31 35216 0"

func main() {
	part2(data)
}

func part1(initial string) {
	stones := strings.Fields(initial)

	for i := 0; i < 25; i++ {
		var next []string

		for _, stone := range stones {
			if stone == "0" {
				next = append(next, "1")
			} else if len(stone)%2 == 0 {
				snum2, _ := strconv.Atoi(stone[len(stone)/2:])
				next = append(next, stone[:len(stone)/2], strconv.Itoa(snum2))
			} else {
				snum, _ := strconv.Atoi(stone)
				next = append(next, strconv.Itoa(snum*2024))
			}
			stones = next
		}
		// fmt.Println(stones)
	}

	fmt.Println(len(stones))
}

func digits(num uint64) int {
	i := 0
	for num > 0 {
		num = num / 10
		i++
	}
	return i
}

func round(s uint64, remaining int) []uint64 {
	if remaining == 0 {
		return []uint64{s}
	}
	if s == 0 {
		return round(1, remaining-1)
	} else {
		d := digits(s)
		if d%2 == 0 {
			div := uint64(math.Pow10(d / 2))
			s1 := s / div
			s2 := s % div
			// fmt.Println("splitting", s, d, div, s1, s2)
			return append(round(s1, remaining-1), round(s2, remaining-1)...)
		} else {
			return round(s*2024, remaining-1)
		}
	}
}

func part2(initial string) {
	stones0 := make(map[uint64]uint64)
	stones25 := make(map[uint64]uint64)
	stones50 := make(map[uint64]uint64)
	s25 := make(map[uint64]uint64)
	var r []uint64

	stonesStr := strings.Fields(initial)
	for _, s := range stonesStr {
		us, _ := strconv.ParseUint(s, 10, 64)
		stones0[us] += 1
	}

	// First round
	for stone, count := range stones0 {
		r = round(stone, 25)
		s25[stone] = uint64(len(r))
		for _, res := range r {
			stones25[res] += count
		}
	}

	// Second round
	for stone, count := range stones25 {
		r = round(stone, 25)
		s25[stone] = uint64(len(r))
		for _, res := range r {
			stones50[res] += count
		}
	}

	// Last round, just need number of stones now, not actual
	var sum uint64
	for stone, count := range stones50 {
		if _, ok := s25[stone]; !ok {
			s25[stone] = uint64(len(round(stone, 25)))
		}
		sum += count * s25[stone]
	}
	fmt.Println(stones0)
	println(sum)
}
