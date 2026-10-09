"""Example: one-shot prompting."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Provide one example before the task.
prompt = """
Rewrite the informal sentence in a professional, friendly tone.

Example:
Informal: "Hey, send me that report ASAP."
Professional: "Hello, could you please send me the report as soon as you can?"

Now rewrite this sentence:
Informal: "I can't make it to the meeting, tell everyone."
Professional:
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
