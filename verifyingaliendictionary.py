class Solution:
    def isAlienSorted(self, words, order) -> bool:
        records = []

        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] == words[i + 1][j]:
                    continue
                records.append([words[i][j], words[i + 1][j]])
                break
        print(records)
        if len(records) == 0:
            return False


        for record in records:
            if order.index(record[0]) > order.index(record[1]):
                return False


        return True


m = Solution()

# words = ["hello","leetcode"]
# order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"

m.isAlienSorted(words, order)