use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut complements = HashMap::new();
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            match complements.get(&complement) {
                Some(&index) => return vec![index, i as i32],
                None => {
                    complements.insert(num, i as i32);
                }
            }
        }
        vec![-1, -1]
    }
}
