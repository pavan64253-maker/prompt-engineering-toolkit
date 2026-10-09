"""Example: requesting a concise, checkable calculation."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Ask for the calculation steps rather than an unexplained answer.
prompt = """
A small business has $360 in fixed costs for a batch of products.
Each product costs $6 to make and sells for $18.

Calculate how many products must be sold to cover the fixed costs.
Show the formula, substitute the numbers, and give the result as a whole
number of products. Keep the explanation concise.
"""

# Send the prompt to the model.
response = get_completion(prompt)

# Print the prompt and response.
print("PROMPT:")
print("-" * 50)
print(prompt)
print("\nRESPONSE:")
print("-" * 50)
print(response)
