package main

import "fmt"

func main() {

	num1 := 40
	num2 := 30

	if num1 < num2 {
		fmt.Printf("%v is higher\n", num2)
	} else {
		fmt.Printf("then %v is higher than %v\n", num1, num2)
	}

	for i := 1; i <= 10; i++ {
		fmt.Printf("%v\n", i)
	}

	fmt.Println("Hernan")
	fmt.Printf("Sebastian\n")

	myFunc()

	a := add(1, 1)

	fmt.Printf("%d\n", a)

	b, c := nakedFunc()

	fmt.Printf("%s and %s\n", b, c)

}

func myFunc() {
	name := "Zoe"

	fmt.Printf("%s hi!!\n", name)
}

func add(x int, y int) int {
	return x + y
}

func nakedFunc() (x, y string) {
	x = "Hernan"
	y = "Sebastian"
	return
}
