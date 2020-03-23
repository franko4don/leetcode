class Solution:
    def leastInterval(self, tasks, n) -> int:
        character = [0 for i in range(26)]
        for i in tasks:
            character[ord(i) - ord('A')] += 1
        character.sort()
        max_value = character[len(character) - 1] - 1
        idle_slots = max_value * n
        for i in range(24, -1, -1):
            idle_slots -= min(max_value, character[i])

        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)

m = Solution()
print(m.leastInterval(["A", "A", "A", "B", "B", "B"], 2))

print(ord(''))
