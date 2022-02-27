package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Ingredient struct {
	name       string
	capacity   int
	durability int
	flavor     int
	texture    int
	calories   int
}

func parseIngredients(s string) []Ingredient {
	ingredients := make([]Ingredient, 0)
	for _, line := range strings.Split(s, "\n") {
		words := strings.FieldsFunc(line, split)
		capacity, _ := strconv.Atoi(words[2])
		durability, _ := strconv.Atoi(words[4])
		flavor, _ := strconv.Atoi(words[6])
		texture, _ := strconv.Atoi(words[8])
		calories, _ := strconv.Atoi(words[10])
		ingredients = append(ingredients, Ingredient{
			name:       words[0],
			capacity:   capacity,
			durability: durability,
			flavor:     flavor,
			texture:    texture,
			calories:   calories,
		})
	}
	return ingredients
}

func split(r rune) bool {
	return r == ':' || r == ',' || r == ' '
}

func sum(arr []int) int {
	total := 0
	for _, val := range arr {
		total += val
	}

	return total
}

func getSums(max int, nums []int, list *[][]int, depth int, maxDepth int) {
	if depth > maxDepth {
		return
	}
	s := sum(nums)
	if s == max {
		*list = append(*list, nums)
	}
	if s >= max {
		return
	}
	for i := 0; i < max; i++ {
		cpy := make([]int, len(nums))
		copy(cpy, nums)
		getSums(max, append(cpy, i), list, depth+1, maxDepth)
	}
}

func getScores(cookies [][]int, ingredients []Ingredient, limitCalories bool) map[string]int {
	scores := map[string]int{}
	for _, shares := range cookies {
		aggregate := map[string]int{"capacity": 0, "durability": 0, "flavour": 0, "texture": 0}
		for idx, share := range shares {
			aggregate["capacity"] += share * ingredients[idx].capacity
			aggregate["durability"] += share * ingredients[idx].durability
			aggregate["flavour"] += share * ingredients[idx].flavor
			aggregate["texture"] += share * ingredients[idx].texture
			aggregate["calories"] += share * ingredients[idx].calories
		}
		score := 1
		for key, val := range aggregate {
			if key != "calories" {
				if val < 0 {
					score = 0
					break
				}
				score *= val
			}
		}
		if limitCalories && aggregate["calories"] != 500 {
			score = 0
		}
		scores[fmt.Sprintf("%v", shares)] = score
	}
	return scores
}

func main() {
	dat, _ := os.ReadFile("./input.txt")
	ingredients := parseIngredients(string(dat))
	tsp := 100
	cookies := make([][]int, 0)
	getSums(tsp, []int{}, &cookies, 0, len(ingredients))

	scores := getScores(cookies, ingredients, false)
	max := 0
	shares := ""
	for key, val := range scores {
		if val > max {
			max = val
			shares = key
		}
	}
	fmt.Printf("Part 1 - %s: %d\n", shares, max)

	scores = getScores(cookies, ingredients, true)
	max = 0
	shares = ""
	for key, val := range scores {
		if val > max {
			max = val
			shares = key
		}
	}
	fmt.Printf("Part 2 - %s: %d\n", shares, max)
}
