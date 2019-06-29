class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map_1 = {}
        for i in range(len(list1)):
            map_1[list1[i]] = i
        result = []
        min_val = 3000
        for i in range(len(list2)):
            if list2[i] in map_1:
                if map_1[list2[i]] + i < min_val:
                    min_val = map_1[list2[i]] + i
                    result = [list2[i]]
                elif map_1[list2[i]] + i == min_val:
                    result.append(list2[i])
        return result
