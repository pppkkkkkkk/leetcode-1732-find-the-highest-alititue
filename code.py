class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        hAli = 0
        cur = 0 
        for num in gain:
            cur += num
            hAli = max(hAli, cur)
        return hAli