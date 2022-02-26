package main

import (
	"fmt"
	"math"
)

func main() {
	input := "hxbxwxba"
	pass := getNextPass(input)
	fmt.Printf("Part 1: %s\n", pass)
	passChars := []rune(getNextPass(pass))
	incrementChars(&passChars, 1)
	pass = getNextPass(string(passChars))
	fmt.Printf("Part 2: %s\n", pass)

}

func getNextPass(input string) string {
	var chars []rune
	for i := 0; i < len(input); i++ {
		chars = append(chars, rune(input[i]))
	}

	valid := false
	for !valid {
		increment := 0
		valid = true
		if !checkDoubleLetters(chars) {
			// Increment till satisfied
			valid = false
			var diff rune
			for i := len(chars) - 1; i > 1; i-- {
				diff = chars[i-1] - chars[i]
				if diff < 0 {
					diff = 1
					break
				} else if diff > 0 {
					diff = diff % 26
					break
				} else {
					continue
				}
			}
			increment = int(diff)
			incrementChars(&chars, increment)
		}

		if !checkIncreasingStraight(chars) {
			increment = 1
			valid = false
			incrementChars(&chars, increment)
		}

		check, pos := checkNoIllegalChars(chars, []rune{'i', 'o', 'l'})
		if !check {
			// increment till satisfied
			valid = false
			diff := (math.Pow(26, float64(len(chars)-pos-1)))
			increment = int(diff)
			incrementChars(&chars, increment)
			for i := pos + 1; i < len(chars); i++ {
				chars[i] = 'a'
			}
		}
	}
	return fmt.Sprintf("%s", string(chars))
}

func incrementChars(chars *[]rune, increment int) {
	carry := 0
	for i := len(*chars) - 1; i >= 0; i-- {
		if i == len(*chars)-1 {
			(*chars)[i] += rune(increment)
		} else {
			(*chars)[i] += rune(carry)
			carry = 0
		}

		if (*chars)[i] > 'z' {
			carry = int((*chars)[i]-'a') / 26
			(*chars)[i] = (((*chars)[i] - 'a') % 26) + 'a'
		}
	}
}

func checkDoubleLetters(chars []rune) bool {
	var doubleLetter rune
	for i := 1; i < len(chars); i++ {
		if chars[i] == chars[i-1] {
			if doubleLetter == 0 {
				doubleLetter = chars[i]
			} else if chars[i] != doubleLetter {
				return true
			}

		}
	}
	return false
}

func checkIncreasingStraight(chars []rune) bool {
	if len(chars) < 3 {
		return false
	}
	for i := 2; i < len(chars); i++ {
		if chars[i]-1 == chars[i-1] && chars[i-1]-1 == chars[i-2] {
			return true
		}
	}
	return false
}

func checkNoIllegalChars(chars []rune, illegal []rune) (bool, int) {
	for i := 0; i < len(chars); i++ {
		for j := 0; j < len(illegal); j++ {
			if chars[i] == illegal[j] {
				return false, i
			}
		}
	}
	return true, -1
}
