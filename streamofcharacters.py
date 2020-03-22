
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end = True

    def search(self, word):
        current = self.root
        for ch in word:

            if ch not in current.children:
                return False
            current = current.children[ch]
            if current.end:
                return True

        return current.end


class StreamChecker:

    def __init__(self, words):

        self.query1 = []
        self.last = 0
        self.trie = Trie()
        for word in words:
            word = list(word)
            word.reverse()
            word = ''.join(word)
            self.trie.insert(word)

    def query(self, letter):
        self.query1.append(letter)
        query1 = self.query1[self.last:]
        query1.reverse()
        found = self.trie.search(''.join(query1))
        return found

# ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query"]
# [[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]

# Your StreamChecker object will be instantiated and called as such:
# words = ["cd", "f", "kl"]
streamChecker = StreamChecker(["ab","ba","aaab","abab","baa"])
# print(streamChecker.home())
streamChecker.query("a")
streamChecker.query('a');
streamChecker.query('a');
streamChecker.query('a');
streamChecker.query('a');
streamChecker.query('b');
streamChecker.query('a');
streamChecker.query('b');
streamChecker.query('b');
streamChecker.query('b');
streamChecker.query('a');
streamChecker.query('b');