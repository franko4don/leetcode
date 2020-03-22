from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)

        if not wordList.__contains__(endWord):
            return 0
        queue = deque()
        queue.append(beginWord)
        count = 1
        char = string.ascii_lowercase

        while len(queue) > 0:
            for m in range(len(queue)):
                n = queue.popleft()
                for i in range(len(n)):
                    nword = list(n)
                    # original = nword[i]
                    for ch in char:
                        nword[i] = ch
                        lw = ''.join(nword)
                        if lw == endWord:
                            return count + 1
                        if wordList.__contains__(lw) and lw != n:
                            print(lw)
                            queue.append(lw)
                            wordList.remove(lw)
            count += 1
        return 0

start = 'hit'
end = 'cog'
lst = ["hot","dot","dog","lot","log","cog"]
# start = "a"
# end = "c"
# lst = ["a","b","c"]

s = Solution()
print(s.ladderLength(start, end, lst))