#!/usr/bin/python3
"""
Test script for the multiply_list_map function.
"""
import importlib.util
import sys
import os

# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))
# Build the full path to the module file
module_path = os.path.join(current_dir, '11-multiply_list_map.py')

# Set up the module spec
spec = importlib.util.spec_from_file_location('multiply_list_map_module', module_path)
# Create the module
module = importlib.util.module_from_spec(spec)
# Add the module to sys.modules
sys.modules['multiply_list_map_module'] = module
# Execute the module
spec.loader.exec_module(module)

# Get the function from the module
multiply_list_map = module.multiply_list_map

# Test case 1: Normal list and number
test_list1 = [1, 2, 3, 4]
multiplier1 = 3
result1 = multiply_list_map(test_list1, multiplier1)
print(f"Test 1 - Normal list {test_list1} * {multiplier1}: {result1}")
# Expected output: [3, 6, 9, 12]

# Test case 2: None as input
result2 = multiply_list_map(None, 5)
print(f"Test 2 - None as input * 5: {result2}")
# Expected output: []

# Test case 3: Empty list
test_list3 = []
multiplier3 = 10
result3 = multiply_list_map(test_list3, multiplier3)
print(f"Test 3 - Empty list [] * {multiplier3}: {result3}")
# Expected output: []

# Test case 4: List with different number types
test_list4 = [1, 2.5, -3, 0]
multiplier4 = 2
result4 = multiply_list_map(test_list4, multiplier4)
print(f"Test 4 - Mixed numbers {test_list4} * {multiplier4}: {result4}")
# Expected output: [2, 5.0, -6, 0]

# Additional test case: Default parameters
result5 = multiply_list_map()
print(f"Test 5 - Default parameters: {result5}")
# Expected output: []

