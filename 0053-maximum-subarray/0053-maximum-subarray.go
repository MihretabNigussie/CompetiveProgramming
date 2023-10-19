import "math"

func maxSubArray(nums []int) int {
	currSum := 0
	maxSum := math.Inf(-1)

	for _, num := range nums {
		if currSum < 0 {
			currSum = 0
		}
		currSum += num
		maxSum = math.Max(float64(maxSum), float64(currSum))
	}

	return int(maxSum)
}