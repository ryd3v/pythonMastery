# Compound Interest Calculator

# Get user input
p = float(input("How much $ are you investing? "))  # Convert to float
r = float(input("What is the interest rate % (just enter the number)? ")) / 100  # Convert to decimal
t = float(input("How many years? "))

# Display compounding options
print("What is the compounding frequency? ")
print("1. Annually (once a year)")
print("2. Semi-Annually (twice a year)")
print("3. Quarterly (four times a year)")
print("4. Monthly (twelve times a year)")
print("5. Daily (365 times a year)")

# Get the user's choice for compounding frequency
n_options = {1: 1, 2: 2, 3: 4, 4: 12, 5: 365}
n_choice = int(input("Choose an option (1-5): "))
n = n_options.get(n_choice, 1)  # Defaults to annually if an invalid option is chosen

# Calculate compound interest
compound_interest = p * (1 + r / n) ** (n * t)

# Print the result
print(f"The compound interest is: {compound_interest:.2f}")
