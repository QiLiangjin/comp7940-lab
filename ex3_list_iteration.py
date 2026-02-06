# Function to find and print all factors of a number
def print_factor(x):
    """Prints all factors of the given number x"""
    factors = []
    
    for i in range(1, x + 1):  # Loop from 1 to x (inclusive)
        if x % i == 0:         # If x is divisible by i
            factors.append(i)  # i is a factor of x
    
    print(f"All factors of {x}: {factors}")
    return factors  # Return the list of factors

# List of numbers
l = [52633, 8137, 1024, 999]

# Apply the function to each number in the list
print("Finding factors for all numbers in the list:")
for number in l:
    print_factor(number)
    print("-" * 40)