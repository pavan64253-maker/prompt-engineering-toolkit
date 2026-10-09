"""Example: zero-shot chain-of-thought style prompting."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Ask for a step-by-step, auditable solution without giving examples.
prompt = """
I have $240 saved and want to reach $600. If I save $30 each week,
how many full weeks will it take to reach my goal?
Show the arithmetic in a few clear steps and state the final number of weeks.
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
