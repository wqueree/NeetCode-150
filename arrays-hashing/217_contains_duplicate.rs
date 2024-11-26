use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut appearances = HashSet::with_capacity(nums.len());
        for num in nums {
            if !appearances.insert(num) {
                return true;
            }
        }
        false
    }
}
