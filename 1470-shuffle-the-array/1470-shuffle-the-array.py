class Solution(object):
    def shuffle(self, nums, n):
        
        # Store x and y together in each first-half element
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i + n]

        # Decode from the back
        j = 2 * n - 1

        for i in range(n - 1, -1, -1):
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10

            nums[j] = y
            nums[j - 1] = x

            j -= 2

        return nums