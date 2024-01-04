with open('test.txt','r') as file:
    nums = file.readlines()
    nums = [ int(x[:-1]) for x in nums ]
avg = sum(nums)/len(nums)
print(avg)