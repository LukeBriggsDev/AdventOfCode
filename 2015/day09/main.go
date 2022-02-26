package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func panicOnError(e error) {
	if e != nil {
		panic(e)
	}

}

func main() {
	data, err := os.ReadFile("./input.txt")
	panicOnError(err)

	table := buildAdjacencyMap(string(data))
	routes := make([]int, 0)
	for place := range table {
		path := make([]string, 0)
		getShortestRoute(place, table, path, 0, &routes)
	}
	sort.Ints(routes)
	min := routes[0]
	max := routes[0]
	for _, dist := range routes {
		if dist < min {
			min = dist
		} else if dist > max {
			max = dist
		}
	}
	fmt.Printf("Longest: %#v\n", max)
	fmt.Printf("Shortest: %#v\n", min)
}

func getShortestRoute(node string, places map[string]map[string]int, path []string, dist int, routes *[]int) {
	path = append(path, node)

	// Add length from current to last node
	if len(path) > 1 {
		dist += places[(path)[len(path)-2]][node]
	}

	// If path contains all return.
	if len(places) == len(path) {
		fmt.Printf("%#v, %d\n", path, dist)
		*routes = append(*routes, dist)
		return
	}

	// Fork paths for all possible cities not yet used
	for place := range places {
		containsPlace := false
		for _, i := range path {
			if i == place {
				containsPlace = true
				break
			}
		}

		_, exists := places[place][node]
		if !containsPlace && exists {
			getShortestRoute(place, places, path, dist, routes)
		}
	}
}

func buildAdjacencyMap(data string) map[string]map[string]int {
	list := strings.Split(string(data), "\n")
	table := make(map[string]map[string]int)
	for _, travel := range list {
		splitTravel := strings.Split(travel, " ")
		src := splitTravel[0]
		dst := splitTravel[2]
		dist, err := strconv.Atoi(splitTravel[4])
		panicOnError(err)

		_, present := table[src]
		if !present {
			table[src] = make(map[string]int)
		}

		_, present = table[dst]
		if !present {
			table[dst] = make(map[string]int)
		}
		table[src][dst] = dist
		table[dst][src] = dist

	}
	return table
}
