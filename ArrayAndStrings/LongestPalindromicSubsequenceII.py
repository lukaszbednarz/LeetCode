class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)

        prev = [(0, None)] * n


        for i in range(n -1 , -1, -1):
            curr = [(0, None)] * n
            for j in range(i + 1, n):
                if s[i] == s[j] != prev[j - 1][1]:
                    curr[j] = (2 + prev[j - 1][0], s[i])
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        return curr[-1][0]




if __name__ == '__main__':
    sol = Solution()

    s = "dcbccacdb"

    output = sol.longestPalindromeSubseq(s)

    print(output)

