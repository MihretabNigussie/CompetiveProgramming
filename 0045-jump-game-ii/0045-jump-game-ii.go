import "math"

func jump(nums []int) int {
	count := 0
	left, right := 0, 0

	for right < len(nums)-1 {
		furthest := 0

		for i := left; i <= right; i++ {
			furthest = int(math.Max(float64(furthest), float64(i+nums[i])))
		}

		left = right + 1
		right = furthest
		count++
	}

	return count
}