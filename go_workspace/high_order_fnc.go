package main

import "fmt"

// Using high order functions with function output parameters
func addHundred(x int) int {
	return x + 100
}

func partialSum(x ...int) func() {
	sum := 0
	for _, value := range x {
		sum += value
	}
	return func() {
		fmt.Println(addHundred(sum))
	}
}

// Using high order functions with integer output parameters
func addHundred_v2(x int) int {
	return x + 100
}

func partialSum_v2(add100 func(x int) int, x ...int) int {
	sum := 0
	for _, value := range x {
		sum += value
	}
	return add100(sum)
}

func main() {
	partial := partialSum(1, 2, 3, 4, 5)
	partial()

	partial2 := partialSum_v2(addHundred_v2, 1, 2, 3)
	fmt.Println(partial2)
}
