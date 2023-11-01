func diagonalSum(mat [][]int) int {
    res := 0 
    var n int = len(mat)
    for i := 0 ; i < n; i ++{
        res += mat[i][i]
        res += mat[i][len(mat)- 1 - i]
    }
    if n % 2 == 0{
        return res 
    } else{
        return res - (mat[n / 2][n / 2])
    }
}