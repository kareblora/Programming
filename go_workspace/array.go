package main

import "fmt"

func main() {
	// arr := [5]bool{true, true, true, true}
	//	for i := 0; i < len(arr); i++ {
	//		if arr[i] {
	//			fmt.Println(i)
	//		}
	//	}

	// arr := [5]string{"a", "b", "c", "d", "e"}
	// slice := arr[:4]
	// fmt.Println(arr)
	// fmt.Println(slice)
	// slice[1] = "x"
	// fmt.Println(arr)
	// fmt.Println(slice)

	arr := []int{10, 20, 90, 70, 60}
	slice := make([]int, 10)
	copy(slice, arr)
	slice[1] = 1000
	fmt.Println(arr)
	fmt.Println(slice)

}
