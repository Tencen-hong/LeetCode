class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = dict()
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1
        word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], x))
        return [w for w, _ in word_dict[:k]]
