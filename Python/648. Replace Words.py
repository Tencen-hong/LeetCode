class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        rootset = set(dict)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))