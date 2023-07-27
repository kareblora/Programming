package main

import "fmt"

type Movie struct {
	name   string
	rating float32
}

func main() {
	m := Movie{name: "ABCD"}
	var m2 Movie
	fmt.Printf("%+v \n", m)
	fmt.Printf("%+v \n", m2)
}
