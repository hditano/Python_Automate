package main

import (
	"fmt"
)

func main() {
	var a [5][5]int
	a[0][0] = 10
	a[4][1] = 100

	var c float32 = 10.2
	var d int8
	var e = []int {10,20,30,40}
	var f []int
	f = append(f, 20)

	var g = []int {300,500}
	f = append(f, g...)

	var myArray = [4]int{1,2,3}
	var mySlice = make([]int, len(myArray))

	// Copy Array to Slice

	copy(mySlice, myArray[:])

	// Map

	m :=map [string]int {
		"Hernan": 39,
	}

	fmt.Printf("float: %f - int: %d\n", c, d)
	fmt.Println("Convirtiendo float to int")
	fmt.Printf("old float: %f - new float: %d\n", c, int(c))
	fmt.Printf("Slice value is : %v\n", len(e))
	fmt.Printf("Array value is: %v\n", f)
	fmt.Printf("My array is: %v\n", myArray)
	fmt.Printf("Array copied to Slice: %v\n", mySlice)
	fmt.Printf("My map: %v\n", m)

	v, ok := m["Hernan"]
	fmt.Println(v, ok)


	type person struct {
		name string
		age int
	}

	n := person {
		name: "Hernan",
		age: 30,
	}

	fmt.Println(n)

	fmt.Println("Cambiamos el valor de la struct")
	fmt.Printf("n.name: %v , n.age: %v\n", n.name, n.age)

	n.name = "Zoe"

	fmt.Printf("Nuevo valor de n.name: %v\n", n.name)

	// Loop Array/Slice

	for i, item := range e{
		fmt.Println(i, item)
	}

	var o string = "Hernan"

	switch o {
	case "Hernan":
		fmt.Println("Gratz Hernan!!")
	default:
	  fmt.Println("Everything else")
	}

	


	for _, item := range a {
		for _, items := range item {
			if items == 100 {
				fmt.Printf("%v\n", items)
			}
		}
	}
}
