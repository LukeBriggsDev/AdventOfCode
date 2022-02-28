package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

func printGrid(grid [][]bool, includeDelay bool) {
	fmt.Printf("\033[0;0H")
	for _, row := range grid {
		for _, col := range row {
			if col {
				fmt.Print("#")
			} else {
				fmt.Print(".")
			}
		}
		fmt.Print("\n")
	}

	if includeDelay {
		time.Sleep(100 * time.Millisecond)
	}

}

func tick(grid [][]bool, cornersAlwaysOn bool) [][]bool {
	newGrid := make([][]bool, len(grid))

	for row := range grid {
		for col := range grid[row] {
			// Count neighbours that are on
			count := 0
			for diffy := -1; diffy <= 1; diffy++ {
				for diffx := -1; diffx <= 1; diffx++ {
					if !(diffy == 0 && diffx == 0) &&
						row+diffy >= 0 &&
						col+diffx >= 0 &&
						row+diffy < len(grid) &&
						col+diffx < len(grid[row]) &&
						grid[row+diffy][col+diffx] {
						count += 1
					}
				}
			}

			if grid[row][col] {
				if count == 2 || count == 3 {
					newGrid[row] = append(newGrid[row], true)
				} else if cornersAlwaysOn && (row == 0 || row == len(grid)-1) && (col == 0 || col == len(grid[row])-1) {
					newGrid[row] = append(newGrid[row], true)
				} else {
					newGrid[row] = append(newGrid[row], false)
				}
			} else {
				if count == 3 {
					newGrid[row] = append(newGrid[row], true)
				} else {
					newGrid[row] = append(newGrid[row], false)
				}
			}

		}
	}

	return newGrid
}

func main() {
	dat, _ := os.ReadFile("./input.txt")
	str := string(dat)

	lines := strings.Split(str, "\n")
	grid := make([][]bool, len(lines))

	for idx, line := range lines {
		for _, char := range line {
			if char == '#' {
				grid[idx] = append(grid[idx], true)
			} else {
				grid[idx] = append(grid[idx], false)
			}
		}
	}

	// Part 1
	grid1 := make([][]bool, len(lines))
	copy(grid1, grid)
	for i := 0; i < 100; i++ {
		printGrid(grid1, false)
		grid1 = tick(grid1, false)
	}

	total1 := 0
	for _, row := range grid1 {
		for _, col := range row {
			if col {
				total1 += 1
			}
		}
	}

	// Part 2
	grid2 := make([][]bool, len(lines))
	copy(grid2, grid)
	for i := 0; i < 100; i++ {
		printGrid(grid2, false)
		grid2 = tick(grid2, true)
	}

	total2 := 0
	for _, row := range grid2 {
		for _, col := range row {
			if col {
				total2 += 1
			}
		}
	}
	fmt.Printf("Part 1: %d\nPart 2: %d\n", total1, total2)

}
