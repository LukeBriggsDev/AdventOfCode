package main

import (
	"fmt"
	"strconv"
)

func lookAndSay(num string) string {
	str := ""
	count := 0
	for i := 0; i < len(num)-1; i++ {
		l := num[i]
		r := num[i+1]
		count += 1
		if i+1 == len(num)-1 {
			if l == r {
				count += 1
			}
			str = str + strconv.Itoa(count) + string(l)
			if l != r {
				str = str + "1" + string(r)
			}

		} else if l != r {
			str = str + strconv.Itoa(count) + string(l)
			count = 0
		}
	}
	return str
}

func main() {
	input := "1113122113"
	for i := 0; i < 40; i++ {
		input = lookAndSay(input)
		fmt.Printf("%d\n", len(input))
	}
}
