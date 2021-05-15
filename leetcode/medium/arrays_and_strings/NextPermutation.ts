/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutationTS(nums: number[]): void {
    if (nums.length < 2) {
        return;
    }
    for (var i = nums.length - 1; i > 0 && nums[i - 1] >= nums[i]; i--);
    if (i == 0) {
        nums.sort((x, y) => x - y);
        return;
    }
    let aux = nums.slice(i).sort((x, y) => x - y);
    for (let k = 0; k < aux.length; k++) {
        nums[i + k] = aux[k];
    }
    for (var j = i; j < nums.length && nums[i - 1] >= nums[j]; j++);
    [nums[i - 1], nums[j]] = [nums[j], nums[i - 1]];
}