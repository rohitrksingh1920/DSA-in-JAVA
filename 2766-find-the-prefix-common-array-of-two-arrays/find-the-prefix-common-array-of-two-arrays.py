class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        result = []
        seen = set()
        common = 0

        for i in range(n):

            if A[i] in seen:
                common += 1
            seen.add(A[i])

            if B[i] in seen:
                common += 1
            seen.add(B[i])

            result.append(common)

        return result