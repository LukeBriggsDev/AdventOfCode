package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type aunt struct {
	children    int
	cats        int
	samoyeds    int
	pomeranians int
	akitas      int
	vizslas     int
	goldfish    int
	trees       int
	cars        int
	perfumes    int
}

func split(r rune) bool {
	return r == ':' || r == ' ' || r == ','
}

func parseAunts(file string) []map[string]int {
	auntList := make([]map[string]int, 0)

	dat, _ := os.ReadFile(file)
	for _, line := range strings.Split(string(dat), "\n") {
		aunt := make(map[string]int)
		aunt["children"] = -1
		aunt["cats"] = -1
		aunt["samoyeds"] = -1
		aunt["pomeranians"] = -1
		aunt["akitas"] = -1
		aunt["vizslas"] = -1
		aunt["goldfish"] = -1
		aunt["trees"] = -1
		aunt["cars"] = -1
		aunt["perfumes"] = -1
		split := strings.FieldsFunc(line, split)

		for i := 2; i < len(split)-1; i += 2 {
			aunt[split[i]], _ = strconv.Atoi(split[i+1])
		}

		auntList = append(auntList, aunt)
	}

	return auntList

}
func main() {
	auntList := parseAunts("./input.txt")

	correctAunt := map[string]int{
		"children":    3,
		"cats":        7,
		"samoyeds":    2,
		"pomeranians": 3,
		"akitas":      0,
		"vizslas":     0,
		"goldfish":    5,
		"trees":       3,
		"cars":        2,
		"perfumes":    1,
	}

	answer1 := 0
	answer2 := 0

	for idx, aunt := range auntList {
		isCorrect1 := true
		isCorrect2 := true
		for key, val := range aunt {
			for correctKey, correctVal := range correctAunt {

				if key == correctKey {
					// Part 1
					if val != correctVal && val != -1 {
						isCorrect1 = false
					}
					// Part 2
					if key == "cats" || key == "trees" {
						if val <= correctVal && val != -1 {
							isCorrect2 = false
						}
					} else if key == "pomeranians" || key == "goldfish" {
						if val >= correctVal && val != -1 {
							isCorrect2 = false
						}
					} else if val != correctVal && val != -1 {
						isCorrect2 = false
					}
				}
			}
		}
		if isCorrect1 {
			answer1 = idx + 1
		}
		if isCorrect2 {
			answer2 = idx + 1
		}
	}

	fmt.Printf("Part 1: %d\n", answer1)
	fmt.Printf("Part 2: %d\n", answer2)
}
