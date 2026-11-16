# ------------ DAY 1 _________
#
# def find_target_pair(nums, target):
#     if nums == []:
#         return [-1, -1]
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return [-1, -1]
#
# def find_target_pair_Optimized(nums, target):
#     storage = {}
#     if nums == []:
#         return [-1, -1]
#     for i in range(len(nums)):
#         ans = target - nums[i]
#         if ans in storage:
#             return [storage[ans], i]
#         else:
#             storage[nums[i]] = i
#

#------------------------optimal and  profination code  -----------------------------------

# def find_target_pair(nums: list[int], target: int) -> list[int]:
#     """
#     Finds two distinct indices whose values sum to the target.
#     Time Complexity: O(n) - single pass with O(1) hash map operations.
#     Space Complexity: O(n) - stores up to n elements in the dictionary.
#     """
#     seen: dict[int, int] = {}  # maps value -> index
#
#     for current_idx, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], current_idx]
#         seen[num] = current_idx
#
#     return []
#
#
# nums = [2, 7, 11, 15]
# target = 9
# # print(find_target_pair(nums, target))
# print(find_target_pair(nums, target))


#__________________ day 2 ________________
#
# def find_pair_sorted (number, target):
#     l =0
#     r = len(number) -1
#     while l < r:
#         ans = number[l] + number[r]
#         if target == ans:
#             return [l +1, r + 1]
#         elif target > ans:
#             l += 1
#         else:
#             r -= 1
#     return[]
#
#
# numbers = [2, 7, 11, 15]
# target = 9
# print(find_pair_sorted(numbers, target))
# # Output: [1, 2] (1-indexed)


# ____________________ DAY 3 -------------------

def max_sub_array_sum(nums: list[int], k: int) -> int:
    if len(nums) < k or k <= 0:
        return 0

    # Step 1: Compute the sum of the very first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Step 2: Slide the window across the rest of the array
    for i in range(k, len(nums)):
        # Subtract the element falling out of the window (nums[i - k])
        # Add the new element entering the window (nums[i])
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Test
print(max_sub_array_sum([2, 1, 5, 1, 3, 2], 3))  # Output: 9 (from [5, 1, 3])