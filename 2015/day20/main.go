package main

import (
	"fmt"
)

func part1(target int) {
	house := 0
	for true {
		house++
		score := 0
		for i := 1; i <= house; i++ {
			if house%i == 0 {
				score += 10 * i
			}
		}
		fmt.Printf("%d, %d\n", house, score)
		if score > target {
			fmt.Println("Solution: ", house)
			break
		}
	}
}

func part2(target int) {
	house := 0
	counter := []int{0, 0}
	for true {
		house++
		score := 0
		for i := 1; i <= house; i++ {
			if house%i == 0 {
				if len(counter) <= i {
					counter = append(counter, 0)
				}
				if counter[i] < 50 {
					counter[i]++
					score += 11 * i
				}
			}
		}
		fmt.Printf("%d, %d\n", house, score)
		if score > target {
			fmt.Println("Solution: ", house)
			break
		}
	}
}

func main() {
	target := 33100000
	//part1(target)
	part2(target)

}
