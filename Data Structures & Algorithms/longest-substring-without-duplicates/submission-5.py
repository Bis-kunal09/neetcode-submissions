
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        i, j = 0, 0
        ans = 0

        while j < len(s):
            if s[j] not in map:
                map[s[j]] = 1
            else:
                while s[j] in map:
                    map[s[i]] -= 1
                    if map[s[i]] == 0:
                        del map[s[i]]
                    i += 1

                map[s[j]] = 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans
