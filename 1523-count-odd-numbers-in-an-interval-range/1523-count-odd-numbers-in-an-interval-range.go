func countOdds(low int, high int) int {
    length := high - low + 1
    var count int = length / 2
    if length % 2 != 0 && low % 2 != 0{
        count += 1
    }
    return count
}