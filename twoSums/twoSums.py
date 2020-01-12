# tags: array, generator, moving window method

# problem description: 

class Solution(object):
   def twoSums(nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      for i in range(len(nums)):
          for j in range(i+1,len(nums)):
              if nums[i]+nums[j]==target:
                  return i, j
              j+=1
          i+=1

