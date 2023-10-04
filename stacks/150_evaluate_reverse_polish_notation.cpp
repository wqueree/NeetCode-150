#include <stack>
#include <string>
#include <unordered_set>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> values;
        std::unordered_set<std::string> operators {std::string {"+"}, std::string {"-"}, std::string {"*"}, std::string {"/"}};
        for (std::string& token : tokens) {
            if (operators.find(token) != operators.end()) {
                int right = values.top();
                values.pop();
                int left = values.top();
                values.pop();
                if (token == "+") {
                    values.push(left + right);
                }
                else if (token == "-") {
                    values.push(left - right);
                }
                else if (token == "*") {
                    values.push(left * right);
                }
                else {
                    values.push(static_cast<int>(left / right));
                }
            }
            else {
                values.push(std::stoi(token));
            }
        }
        return values.top();
    }
};