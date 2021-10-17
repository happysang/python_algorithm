#https://velog.io/@happysang/%EB%B0%B0%EC%97%B4

from typing import List
def three_sum1(nums:List[List[int]]):
    result = []
    nums.sort()
    #브루트 포스 n^3반복
    for i in range (len(nums) - 2):
        #중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j > i + i and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    return result
#print(three_sum1([-1, 0, 1, 2, -1, -4]))



def three_sum2(nums:List[List[int]]):
    result = []
    nums.sort()
    for i in range (len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1

        while(left < right):
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
    return result
#print(three_sum2([-1, 0, 1, 2, -1, -4]))



def product_except_self1(nums):
    res = []
    for x in range(len(nums)):
        mul = 1
        for y in range(len(nums)):
            if x == y:
                continue
            mul *= nums[y]
        res.append(mul)
    return res
#print(product_except_self1([1,2,3,4]))



def product_except_self(nums):
    res = []
    p = 1
    for i in range(len(nums)):
        res.append(p)
        p *= nums[i]
    p = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= p
        p *= nums[i]
    return res
print(product_except_self([1,2,3,4]))



def rain(height):
    res = 0
    left, right = 0, len(height)-1
    l_max, r_max = height[left], height[right]
    while(left < right):
        if l_max <= r_max:
            if height[left+1] > l_max:
                l_max = height[left+1]
            res += (l_max-height[left+1])
            print(f'left : {left}와 {left+1} 사이에 {l_max-height[left+1]}만큼 증가, 값: {res}, l최대:{l_max}, r최대:{r_max}') #어차피 l_max = height[left+1]구나!
            left += 1
        else:
            if r_max <= height[right-1]:
                    r_max = height[right-1]
            res += (r_max-height[right-1])
            print(f'right : {right}와 {right-1} 사이에 {r_max-height[right-1]}만큼 증가, 값: {res}, l최대:{l_max}, r최대:{r_max}')
            right -= 1
    return res
print(rain([0,1,0,2,1,0,1,3,2,1,2,1]))



def trap(height:List[int]):
    if not height:
        return 0
    volume = 0
    left, right = 0, len(height)-1
    l_max, r_max = height[left], height[right]

    while left < right:
        l_max, r_max = max(l_max, height[left]), max(r_max, height[right])

        if l_max <= r_max:
            volume += l_max - height[left]
            left += 1
        else:
            volume += r_max - height[right]
            right -= 1
    return volume
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))