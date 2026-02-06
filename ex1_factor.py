# Find all the factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10 % 3 = 1
x = 52633
factors = []

for i in range(1, x + 1):  # Loop from 1 to x (inclusive)
    if x % i == 0:         # If x is divisible by i (remainder is 0)
        factors.append(i)  # i is a factor of x

print(f"All factors of {x}: {factors}")