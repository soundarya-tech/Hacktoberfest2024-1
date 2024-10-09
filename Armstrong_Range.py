def is_armstrong_number(n):
    # Convert number to string to work with digits
    digits = [int(digit) for digit in str(n)]
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of num_digits
    armstrong_sum = sum(digit ** num_digits for digit in digits)
    
    # Check if the sum equals the original number
    return armstrong_sum == n

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Example usage
start_range = 1
end_range = 1000
armstrong_numbers = find_armstrong_numbers(start_range, end_range)
print(f"Armstrong numbers between {start_range} and {end_range}: {armstrong_numbers}")
