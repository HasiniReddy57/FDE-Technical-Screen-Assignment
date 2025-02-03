def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length
    
    # Determine if the package is bulky or heavy
    bulky = volume >= 1_000_000 or any(d >= 150 for d in (width, height, length))
    heavy = mass >= 20

    # Return the appropriate stack using a ternary operator for concise evaluation
    return (
        "REJECTED" if bulky and heavy 
        else "SPECIAL" if bulky or heavy 
        else "STANDARD"
    )

# Test cases
print(sort(100, 100, 100, 19))  # STANDARD
print(sort(160, 100, 100, 10))  # SPECIAL (bulky)
print(sort(100, 100, 100, 25))  # SPECIAL (heavy)
print(sort(160, 100, 100, 25))  # REJECTED
