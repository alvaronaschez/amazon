func nextPermutation(nums []int)  {
    if len(nums) < 2 {
        return
    }
    var i int
    for i = len(nums) - 1; i > 0 && nums[i - 1] >= nums[i]; i-- {}
    if (i == 0) {
        sort.Ints(nums)
        return
    }
    aux := nums[i:]
    sort.Ints(aux)
    for k, e := range aux {
        nums[i + k] = e
    }
    var j int
    for j = i; j < len(nums) && nums[i - 1] >= nums[j]; j++ {}
    nums[i - 1], nums[j] = nums[j], nums[i - 1]
}