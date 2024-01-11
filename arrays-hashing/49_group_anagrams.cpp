#include <algorithm>
#include <vector>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> group_map {};
        for (const std::string& str : strs) {
            std::string sorted_str = std::string {str};
            std::sort(sorted_str.begin(), sorted_str.end());
            group_map[sorted_str].push_back(str);
        }
        std::vector<std::vector<std::string>> groups;
        for (const auto& [sorted_str, str_groups] : group_map) {
            groups.push_back(str_groups);
        }
        return groups;
    }
};
