#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](std::vector<int> a, std::vector<int> b) {return a[0] < b[0];});
        std::vector<std::vector<int>> merge_intervals {};
        for (const std::vector<int>& interval : intervals) {
            if (merge_intervals.size() == 0 || interval[0] > merge_intervals.back()[1]) {
                merge_intervals.push_back(interval);
            }
            else if (interval[1] > merge_intervals.back()[1]) {
                merge_intervals.back()[1] = interval[1];
            }
        }
        return merge_intervals;
    }
};
