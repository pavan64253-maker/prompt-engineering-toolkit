"""Example: representing system, user, and assistant roles in a prompt."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# This helper accepts a text prompt, so role instructions are labeled explicitly.
system_instruction = (
    "You are a helpful writing coach. Be concise, encouraging, and practical."
)
user_request = (
    "I want to start a daily reading habit but only have 15 minutes a day. "
    "Suggest one simple plan."
)
prompt = f"""
SYSTEM:
{system_instruction}

USER:
{user_request}

ASSISTANT:
"""

# Send the role-labeled prompt to the model.
response = get_completion(prompt)

# Print the prompt and the model's response.
print("PROMPT (SYSTEM / USER):")
print("-" * 50)
print(prompt)
print("\nASSISTANT RESPONSE:")
print("-" * 50)
print(response)
