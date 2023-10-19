import "strconv"

func fizzBuzz(n int) []string {
	slice := []string{}
	for i := 1; i <= n; i++ {
		if (i%5 == 0) && (i%3 == 0) {
			slice = append(slice, "FizzBuzz")
		} else if i%5 == 0 {
			slice = append(slice, "Buzz")
		} else if i%3 == 0 {
			slice = append(slice, "Fizz")
		} else {
			slice = append(slice, strconv.Itoa(i))
		}
	}
	return slice
}