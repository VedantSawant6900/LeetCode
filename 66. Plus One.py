class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=[str(i) for i in digits]
        number = "".join(digits)
        ans = list(str(eval(number)+1))
        return [int(i) for i in ans]