# Read input numbers as a list of integers
numbers = [int(x) for x in input().split()]

# Filter out negative integers
negative_numbers = [num for num in numbers if num < 0]

# Sort negative integers in descending order
negative_numbers.sort(reverse=True)

# Print the sorted negative integers without extra whitespace at the end
print(*negative_numbers, end=' ')