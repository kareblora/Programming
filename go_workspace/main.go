package main

import (
	"fmt"     // format package
	"reflect" // reflect data types
	"strconv" // String conversion package
)

func main() {
	var grades int = 98 // variable declaration
	var name string
	user := "Kevin" // shorthand variable declaration
	i := strconv.Itoa(grades)

	fmt.Printf("Enter name: ")
	fmt.Scanf("%s", &name)
	fmt.Printf("Hello %s, My name is %s \n", name, user)
	fmt.Printf("Variable grades = %v is of type %v \n", grades, reflect.TypeOf(grades))
	fmt.Printf("Variable i = %v is of type %v \n", i, reflect.TypeOf(i))
}
