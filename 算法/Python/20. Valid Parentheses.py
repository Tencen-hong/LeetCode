class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m_stack = []  # make list as a stack
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':  # push open brackets
                m_stack.append(s[i])
            elif len(m_stack) == 0:  # quantity of open brackets  < close brackets
                return False
            else:
                # open brackets not be closed in the correct order.
                if (s[i] == ')' and m_stack[-1] != '(') or (s[i] == '}' and m_stack[-1] != '{') or (s[i] == ']' and m_stack[-1] != '['):
                    return False
                else:
                    m_stack.pop()
        if len(m_stack) != 0:  # uantity of open brackets  > close brackets
            return False
        return True
