package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	dat, _ := os.ReadFile("./input.txt")
	dict := buildAdjacencyMap(string(dat))
	routes := make([]int, 0)
	path := make([]string, 0)
	getRoutes("David", dict, path, 0, &routes)

	sort.Ints(routes)
	max := routes[len(routes)-1]
	fmt.Printf("Part 1: %#v\n", max)

	// Part 2
	dict["Me"] = make(map[string]int)
	for key, _ := range dict {
		dict["Me"][key] = 0
		dict[key]["Me"] = 0
	}

	routes = make([]int, 0)
	path = make([]string, 0)
	getRoutes("David", dict, path, 0, &routes)
	sort.Ints(routes)
	max = routes[len(routes)-1]
	fmt.Printf("Part 2: %#v\n", max)
}

func getRoutes(node string, people map[string]map[string]int, path []string, happiness int, routes *[]int) {
	path = append(path, node)

	// Add length from current to last node
	if len(path) > 1 {
		// src to dst
		happiness += people[path[len(path)-2]][node]
		// dst to src
		happiness += people[node][path[len(path)-2]]
	}

	// If path contains all, return
	if len(path) == len(people) {
		path = append(path, path[0])
		happiness += people[path[len(path)-2]][path[0]]
		happiness += people[path[0]][path[len(path)-2]]
		*routes = append(*routes, happiness)
		return
	}

	// Fork paths for all possible cities not yet used
	for person := range people {
		containsPerson := false
		for _, i := range path {
			if i == person {
				containsPerson = true
				break
			}
		}

		_, exists := people[person][node]
		if !containsPerson && exists {
			getRoutes(person, people, path, happiness, routes)
		}
	}
}

func buildAdjacencyMap(data string) map[string]map[string]int {
	lines := strings.Split(data, "\n")
	dict := make(map[string]map[string]int)
	for _, line := range lines {
		words := strings.Split(line, " ")
		src := words[0]
		dst := words[10][:len(words[10])-1]
		val, _ := strconv.Atoi(words[3])
		if words[2] == "lose" {
			val *= -1
		}
		_, exists := dict[src]
		if !exists {
			dict[src] = make(map[string]int)
		}

		dict[src][dst] = val
	}
	return dict
}
