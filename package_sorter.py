#!/usr/bin/env python3
"""
Package Sorter Module for Thoughtful’s Robotic Automation Factory

This module provides the `sort_package` function to determine the correct
dispatch stack for a package based on its dimensions and mass.

Dispatch rules:
    - STANDARD: Package is neither bulky nor heavy.
    - SPECIAL: Package is either bulky or heavy (but not both).
    - REJECTED: Package is both bulky and heavy.

A package is considered bulky if:
    - Its volume (width * height * length) is greater than or equal to 1,000,000 cm³, or
    - At least one of its dimensions is greater than or equal to 150 cm.

A package is considered heavy if its mass is greater than or equal to 20 kg.

Note: At least one ternary operator is used in this implementation.
"""

def sort_package(width, height, length, mass):
    """
    Determines the correct dispatch stack for a package.

    Args:
        width (float or int): The width of the package in centimeters.
        height (float or int): The height of the package in centimeters.
        length (float or int): The length of the package in centimeters.
        mass (float or int): The mass of the package in kilograms.

    Returns:
        str: The dispatch stack ("STANDARD", "SPECIAL", or "REJECTED").
    """
    volume = width * height * length

    # Determine if the package is bulky.
    # Using a ternary operator to assign is_bulky.
    is_bulky = True if (volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150) else False

    # Determine if the package is heavy.
    is_heavy = mass >= 20

    # Decision tree based on the package properties.
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# If this module is executed directly, run some test cases.
if __name__ == '__main__':
    # List of test cases in the format:
    # (width, height, length, mass, expected_result)
    test_cases = [
        # Test: Volume = 100*100*100 = 1,000,000 (bulky) but not heavy.
        (100, 100, 100, 10, "SPECIAL"),
        # Test: Width is 200 (>=150) so bulky.
        (200, 50, 50, 15, "SPECIAL"),
        # Test: One dimension is >=150 and mass >=20: bulky and heavy -> rejected.
        (80, 80, 200, 25, "REJECTED"),
        # Test: Volume = 120*120*120 = 1,728,000 (bulky), not heavy.
        (120, 120, 120, 5, "SPECIAL"),
        # Test: Mass is heavy but dimensions are small.
        (50, 50, 50, 30, "SPECIAL"),
        # Test: Both bulky and heavy.
        (200, 200, 200, 30, "REJECTED"),
        # Test: Neither bulky nor heavy.
        (100, 100, 90, 15, "STANDARD")
    ]

    all_passed = True
    for idx, (w, h, l, m, expected) in enumerate(test_cases, start=1):
        result = sort_package(w, h, l, m)
        print(f"Test case {idx}: sort_package({w}, {h}, {l}, {m}) -> {result} (Expected: {expected})")
        if result != expected:
            print(f"  Error: Expected {expected} but got {result}")
            all_passed = False

    if all_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
