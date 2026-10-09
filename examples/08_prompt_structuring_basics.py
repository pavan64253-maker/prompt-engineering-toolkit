"""Example: structuring a prompt with clear sections."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Separate the role, task, context, constraints, and output format.
prompt = """
Role:
You are a practical small-business coach.

Task:
Suggest a simple first-week marketing plan.

Context:
The business sells handmade candles online and has no advertising budget.

Constraints:
- Use free or low-cost actions.
- Keep the plan realistic for one person.
- Avoid vague advice.

Output Format:
Return three numbered actions. For each action, include what to do and why.
"""

# Send the structured prompt to the model.
response = get_completion(prompt)

# Print the prompt and response.
print("PROMPT:")
print("-" * 50)
print(prompt)
print("\nRESPONSE:")
print("-" * 50)
print(response)
