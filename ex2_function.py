# Write a function that prints all factors of the given parameter x
def print_factor(x):
    """Prints all factors of the given number x"""
    factors = []
    
    for i in range(1, x + 1):  # Loop from 1 to x (inclusive)
        if x % i == 0:         # If x is divisible by i
            factors.append(i)  # i is a factor of x
    
    print(f"All factors of {x}: {factors}")

# Example usage:
print_factor(52633)