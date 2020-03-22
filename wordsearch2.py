class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False
        self.value = None


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def buildTrie(self, words):
        for word in words:
            self.insert(word)


    def insert(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end = True
        current.value = word


    def findWords(self, board, words):
        self.buildTrie( words)

        word = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c in self.root.children:
                    self.dfs(board, i, j, self.root, word)
        return word

    def dfs(self, board, i, j, root, word):

        if root.end:
            word.append(root.value)
            # print(root.value)
            root.end = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] == '#':
            return

        temp = board[i][j]

        if temp not in root.children:
            return

        board[i][j] = '#'
        self.dfs(board, i, j + 1, root.children[temp], word)
        self.dfs(board, i, j - 1, root.children[temp], word)
        self.dfs(board, i - 1, j, root.children[temp], word)
        self.dfs(board, i + 1, j, root.children[temp], word)


        board[i][j] = temp


s = Solution()
# data = [["a","b"],["c","d"]]
#
# w = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
data = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
w = ["oath","pea","eat","rain"]

print(s.findWords(data, w))