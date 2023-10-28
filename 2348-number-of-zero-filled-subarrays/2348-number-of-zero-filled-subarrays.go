func zeroFilledSubarray(nums []int) int64 {
    res, count := int64(0), int64(0)
    for i := 0; i < len(nums); i++ {
        if nums[i] == 0 {
            count += 1
        } else {
            count = 0
        }
        res += count
    }
    return res
}