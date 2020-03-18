class Solution {
public:
    bool isValid(string s) {
        stack<char> m_stack;
        for (int i = 0; i < s.size(); i++) {
            switch (s[i]) {
            case '(':
            case '{':
            case '[': m_stack.push(s[i]); break; // push Open brackets
            case ')':
                if (m_stack.empty() || m_stack.top() != '(') // there isn't an Open brackets matching  close brackets
                    return false;
                else
                    m_stack.pop();
                break;
            case '}':
                if (m_stack.empty() || m_stack.top() != '{')
                    return false;
                else
                    m_stack.pop();
                break;
            case ']':
                if (m_stack.empty() || m_stack.top() != '[')
                    return false;
                else
                    m_stack.pop();
                break;
            }
        }
        if (!m_stack.empty()) // left extra open brackets
            return false;
        return true;
    }
};