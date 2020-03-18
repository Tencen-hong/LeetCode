class Solution:
    '''
    按顺序遍历s:
        1.当前元素不是']': 入栈
        2.当前元素是']':弹出栈中的字母并组成字符串，将上述字符串翻转(因为栈先进后出)。
                      继续弹出栈中的数字字符并转成原来顺序的int类型数字，
                      将字符串重复(int数字)次，并一个字符一个字符的入栈。
        3.将栈中所有元素连接起来返回                 
    '''

    def decodeString(self, s: str) -> str:
        string = []
        for i in range(len(s)):
            if s[i] != ']':
                string.append(s[i])
            else:
                temp_string = ""
                while string[-1] != '[':
                    temp_string += string.pop()
                string.pop()
                temp_string = temp_string[::-1]
                temp_num = ""
                while len(string) > 0 and '0' <= string[-1] <= '9':
                    temp_num += string.pop()
                temp_num = int(temp_num[::-1])
                string.extend([it for it in temp_string*temp_num])
        return ''.join(ss for ss in string)
