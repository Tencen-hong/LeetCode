class Solution:
    '''
        1.根据' '和'.'拆分字符串
        2.分别累计各字符串visited值
        3.组合转变为list[str]类型
    '''

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}
        res = []
        for cpdomain in cpdomains:
            space_index = cpdomain.index(' ')
            cnt = int(cpdomain[:space_index])
            domain = cpdomain[space_index+1:]
            while domain:
                if domain not in counter:
                    counter[domain] = 0
                counter[domain] += cnt
                if domain.find('.') == -1:
                    break
                domain = domain[domain.find('.')+1:]
        for k, v in counter.items():
            res.append(str(v)+' ' + str(k))
        return res
