"""Concept example: prompt engineering, prompt tuning, and instruction tuning."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Ask for a beginner-friendly comparison of the three concepts.
prompt = """
Explain the difference between prompt engineering, prompt tuning, and
instruction tuning for a beginner.
For each concept, say what is changed, who typically does it, and give one
short example. End with a brief comparison.
"""

# Send the prompt to the model.
response = get_completion(prompt)

# Print the prompt, model response, and key learning note.
print("PROMPT:")
print("-" * 50)
print(prompt)
print("\nRESPONSE:")
print("-" * 50)
print(response)
print("\nMY NOTE:")
print("-" * 50)
print(
    "Prompt engineering is what API users usually do: write and refine the "
    "input. Prompt tuning and instruction tuning are training-side concepts."
)
