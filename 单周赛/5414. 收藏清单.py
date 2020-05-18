class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        f = [set(x) for x in favoriteCompanies]
        index = [1] * len(f)
        for i in range(len(f)):
            for j in range(len(f)):
                if i != j:
                    if f[i].issubset(f[j]):
                        index[i] = 0
                        break

        return [i for i in range(len(index)) if index[i]]
