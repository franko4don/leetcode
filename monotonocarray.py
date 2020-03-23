class Solution:
    def isMonotonic(self, A) -> bool:
        track1 = True
        track2 = True
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                track1 = False

        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                track2 = False

        return track1 or track2