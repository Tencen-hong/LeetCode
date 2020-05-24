class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, word in enumerate(sentence.split()):
           # print(searchWord,word)
            if len(searchWord) > len(word):
                continue
            f = True

            for i in range(len(searchWord)):
                if searchWord[i] != word[i]:
                    f = False
                    break
            if f:
                return idx+1
        return -1
