#include <iostream>
#include <array>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        std::array<int, 26> s_counts = {0};
        std::array<int, 26> t_counts = {0};
        for (char c : s) {
            s_counts[c - 'a']++;
        }
        for (char c : t) {
            t_counts[c - 'a']++;
        }
        return s_counts == t_counts;
    }
};
