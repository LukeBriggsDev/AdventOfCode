package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	dat, err := os.ReadFile("./input.json")
	if err != nil {
		panic(err)
	}
	var values map[string]interface{}
	json.Unmarshal(dat, &values)
	total := float64(0)
	getNumsMap(values, &total, false)
	fmt.Printf("Part 1: %0.f\n", total)
	total = float64(0)
	getNumsMap(values, &total, true)
	fmt.Printf("Part 2: %0.f\n", total)
}
func getNumsMap(data map[string]interface{}, total *float64, disallowRed bool) {
	if disallowRed {
		for _, val := range data {
			switch val.(type) {
			case string:
				if val.(string) == "red" {
					return
				}
			}
		}
	}
	for _, val := range data {
		switch val.(type) {
		case float64:
			*total += val.(float64)
		case map[string]interface{}:
			getNumsMap(val.(map[string]interface{}), total, disallowRed)
		case []interface{}:
			getNumsArr(val.([]interface{}), total, disallowRed)
		}
	}
}

func getNumsArr(data []interface{}, total *float64, disallowRed bool) {
	for _, val := range data {
		switch val.(type) {
		case float64:
			*total += val.(float64)
		case map[string]interface{}:
			getNumsMap(val.(map[string]interface{}), total, disallowRed)
		case []interface{}:
			getNumsArr(val.([]interface{}), total, disallowRed)
		}
	}
}
