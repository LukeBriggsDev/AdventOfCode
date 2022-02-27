package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type reindeer struct {
	name     string
	speed    int
	flyTime  int
	restTime int
	distance int
	points   int
}

func main() {

	dat, _ := os.ReadFile("./input.txt")
	reindeerList := parseDeer(string(dat))

	part1, part2 := reindeerOlympics(2503, &reindeerList)
	fmt.Printf("Part 1: %d\nPart 2: %d\n", part1, part2)

}

func reindeerOlympics(seconds int, reindeerList *[]reindeer) (int, int) {

	for i := 0; i <= seconds; i++ {
		for idx, deer := range *reindeerList {
			if (i%(deer.flyTime+deer.restTime) + 1) <= deer.flyTime {
				(*reindeerList)[idx].distance += deer.speed
			}
		}

		maxDistance := 0
		for _, deer := range *reindeerList {
			if deer.distance > maxDistance {
				maxDistance = deer.distance
			}
		}

		for idx, deer := range *reindeerList {
			if deer.distance == maxDistance {
				(*reindeerList)[idx].points += 1
			}
		}
	}

	maxDistance := 0
	maxPoints := 0
	for _, deer := range *reindeerList {
		if maxDistance < deer.distance {
			maxDistance = deer.distance
		}
		if maxPoints < deer.points {
			maxPoints = deer.points
		}
	}
	return maxDistance, maxPoints
}

func parseDeer(data string) []reindeer {
	reindeers := make([]reindeer, 0)
	lines := strings.Split(string(data), "\n")
	for _, line := range lines {
		words := strings.Split(line, " ")
		name := words[0]
		speed, _ := strconv.Atoi(words[3])
		flyTime, _ := strconv.Atoi(words[6])
		restTime, _ := strconv.Atoi(words[13])
		deer := reindeer{
			name:     name,
			speed:    speed,
			flyTime:  flyTime,
			restTime: restTime,
			distance: 0,
			points:   0,
		}
		reindeers = append(reindeers, deer)
	}
	return reindeers
}
