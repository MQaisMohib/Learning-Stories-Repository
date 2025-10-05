# Create an empty list (array)
numbers = []

# Input 5 numbers from user
print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

# Display the array elements
print("\nYou entered:", numbers)

# Calculate and display the sum of array elements
total = sum(numbers)
print("Sum of all numbers =", total)

# Find and display the largest number
print("Largest number =", max(numbers))
