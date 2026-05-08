class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []
        count = 0

        for num in nums:
            if num == 0:
                count += 1
            else:
                product *= num
        
        for num in nums:
            if count == 0:
                result.append(product // num)
            elif count == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(0)

        return result