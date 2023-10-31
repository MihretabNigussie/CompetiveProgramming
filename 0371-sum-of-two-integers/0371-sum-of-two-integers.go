func getSum(a int, b int) int {
    for b != 0 {
        temp := (a & b) << 1
        a ^= b
        b = temp
    }
    return a
}