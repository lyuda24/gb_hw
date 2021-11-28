src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_nums = set()
repeated_nums = set()
for num in src:
    if num in repeated_nums:
        continue
    if num in unique_nums:
        repeated_nums.add(num)
        unique_nums.discard(num)
        continue
    unique_nums.add(num)
print([num for num in src if num in unique_nums])
