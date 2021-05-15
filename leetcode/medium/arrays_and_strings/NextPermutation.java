class Solution {
    public void nextPermutation(int[] nums) {
        if(nums.length<2){
            return;
        }
        int i;
        for (i = nums.length - 1; i > 0 && nums[i - 1] >= nums[i]; i--);
        if (i == 0) {
            Arrays.sort(nums);
            return;
        }
        int[] aux = Arrays.copyOfRange(nums, i, nums.length);
        Arrays.sort(aux);
        for (int k = 0; k < aux.length; k++) {
            nums[i + k] = aux[k];
        }
        int j;
        for (j = i; j < nums.length && nums[i - 1] >= nums[j]; j++);
        //swap nums[i-1] and nums[j]
        nums[i-1]=nums[i-1]+nums[j];
        nums[j]=nums[i-1]-nums[j];
        nums[i-1]=nums[i-1]-nums[j];
    }
}