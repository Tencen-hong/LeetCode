class Solution:
    '''
    这个题是走迷宫问题的变形！也就是说，我们每次变化有26个方向，如果变化之后的位置在wordList中，我们认为这个走法是合规的，最后问能不能走到endWord？
    使用了visited来保存已经遍历了的字符串，代表已经走过了的位置。
    直接把已经遍历过的位置从wordList中删除，这样就相当于上面的那个visited数组。
    会在每个节点入队列的时候同时保存了这个节点的深度，这样就少了一层对bfs当前长度的循环，可以使得代码变短。
    '''

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        bfsQueue = collections.deque()
        bfsQueue.append((beginWord, 1))
        while bfsQueue:
            word, length = bfsQueue.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet and newWord != word:
                        wordSet.remove(newWord)
                        bfsQueue.append((newWord, length+1))

        return 0
