# Using a while loop to iterate through a list of numbers and print each number
nums = [12, 45, 67, 89, 23, 90]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


bucket = [34, 56, 78, 90, 12, 23, 45, 34, 34, 34]
x = 90
i=0
while  i < len(bucket):
    if bucket[i] == x:
        print(f"Found the value {x} at index {i}")
    else:
        print("finding...")
    i += 1

# use of continue and break in while
i = 1
while i <= 5:
    print(i)
    if (i == 3):
      break
    i+=1
print("end of loop")

