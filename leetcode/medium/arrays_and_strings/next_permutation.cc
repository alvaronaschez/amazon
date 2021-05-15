#include <algorithm>

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.size()<2){
            return;
        }
        int i;
        for (i = nums.size() - 1; i > 0 && nums[i - 1] >= nums[i]; i--);
        if (i == 0) {
            std::sort(nums.begin(), nums.end());
            return;
        }
        std::sort(nums.begin()+i, nums.end());
        int j;
        for (j = i; j < nums.size() && nums[i - 1] >= nums[j]; j++);
        std::swap(nums[i-1], nums[j]);
    }
};
