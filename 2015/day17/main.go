package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func sumPath(l map[int]int) int {
	total := 0
	for _, val := range l {
		total += val
	}
	return total
}

func getContainers(containerId int, containerVal int, containerList []int, target int, path map[int]int, paths *[]map[int]int, containerLimit int) {

	if containerLimit != -1 && len(path)+1 > containerLimit {
		return
	}

	path[containerId] = containerVal

	if sumPath(path) > target {
		return
	} else if sumPath(path) == target {
		*paths = append(*paths, path)
	}

	for idx, c := range containerList {
		// container not in path
		inPath := false
		for key := range path {
			if key == idx {
				inPath = true
			}
		}

		if !inPath && idx > containerId {
			cpy := make(map[int]int)
			for k, v := range path {
				cpy[k] = v
			}
			getContainers(idx, c, containerList, target, cpy, paths, containerLimit)
		}
	}

}

func main() {
	dat, _ := os.ReadFile("./input.txt")
	strContainers := strings.Split(string(dat), "\n")
	containers := make([]int, 0)
	for _, val := range strContainers {
		num, _ := strconv.Atoi(val)
		containers = append(containers, num)
	}

	paths := make([]map[int]int, 0)
	for idx, val := range containers {
		path := make(map[int]int)
		getContainers(idx, val, containers, 150, path, &paths, -1)
	}

	fmt.Printf("Part 1: %d\n", len(paths))

	leastContainers := len(paths[0])
	for i := 1; i < len(paths); i++ {
		if len(paths[i]) < leastContainers {
			leastContainers = len(paths[i])
		}
	}

	paths = make([]map[int]int, 0)
	for idx, val := range containers {
		path := make(map[int]int)
		getContainers(idx, val, containers, 150, path, &paths, leastContainers)
	}

	fmt.Printf("Part 2: %d\n", len(paths))

}
