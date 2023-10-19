func backspaceCompare(s string, t string) bool {
	stack1 := []rune{}
	stack2 := []rune{}

	for _, value := range s {
		if value != '#' {
			stack1 = append(stack1, value)
		} else if len(stack1) > 0 {
			stack1 = stack1[:len(stack1)-1]
		}
	}

	for _, value := range t {
		if value != '#' {
			stack2 = append(stack2, value)
		} else if len(stack2) > 0 {
			stack2 = stack2[:len(stack2)-1]
		}
	}

	return string(stack1) == string(stack2)
}