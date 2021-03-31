def twoSum(nums, target):
        my_list=[ ]
        for i in range (0, len(nums)-1):
            for j in range(i+1,len(nums) ):
                sum= nums[i]+nums[j]
                if sum==target:
                    my_list.extend([i, j])
        print(my_list)

target=6 
nums= [2,4,5,7,8]
twoSum(nums,target)