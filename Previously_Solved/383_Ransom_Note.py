# Time Complexity: O(m+n)
# Space complexity: O(n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        mag_map = dict()

        for char in magazine:
            if char in mag_map:
                mag_map[char] += 1
            else:
                mag_map[char] = 1

        for char in ransomNote:
            if char not in mag_map:
                return False
            else:
                mag_map[char] -= 1
                if mag_map[char] < 0:
                    return False
        return True
