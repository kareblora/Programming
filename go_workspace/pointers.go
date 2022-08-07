package main

import "fmt"

func modify(y int) int {
	y += 15
	return y
}
func main() {

	var x int
	y := 20
	x = modify(y)
	fmt.Println(x)
}
