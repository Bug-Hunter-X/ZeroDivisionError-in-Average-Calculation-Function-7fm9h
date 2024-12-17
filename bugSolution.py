def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage (This will now return 0, instead of error):
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Example with numbers
my_numbers = [10,20,30]
average = calculate_average(my_numbers)
print(f"The average is: {average}") 