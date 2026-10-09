"""Example: comparing two versions of a reusable prompt."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

task = "Write a product description for a reusable stainless-steel water bottle."

# Version 1 gives only a broad instruction.
prompt_v1 = f"""
Prompt version 1:
{task}
"""

# Version 2 adds audience, useful details, constraints, and a format.
prompt_v2 = f"""
Prompt version 2:
{task}

Audience: Busy commuters who want to reduce single-use plastic.
Details: 750 ml capacity, leak-resistant lid, keeps drinks cold for 12 hours.
Constraints: Use a friendly, factual tone. Do not make claims beyond these details.
Output: One short headline and a description of 40 words or fewer.
"""

# Run both versions against the same task for comparison.
response_v1 = get_completion(prompt_v1)
response_v2 = get_completion(prompt_v2)

# Print each prompt and its response.
print("PROMPT VERSION 1:")
print("-" * 50)
print(prompt_v1)
print("\nRESPONSE VERSION 1:")
print("-" * 50)
print(response_v1)
print("\nPROMPT VERSION 2:")
print("-" * 50)
print(prompt_v2)
print("\nRESPONSE VERSION 2:")
print("-" * 50)
print(response_v2)
