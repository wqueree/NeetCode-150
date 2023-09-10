#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> complements;
        int num;
        int complement;
        for (size_t i = 0; i < nums.size(); ++i) {
            num = nums[i];
            complement = target - num;
            if (complements.find(complement) != complements.end()) {
                return std::vector<int> {complements[complement], (int) i};
            }
            complements[num] = (int) i;
        }
        return std::vector<int> {-1, -1};
    }
};
