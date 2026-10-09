"""Example: few-shot sentiment classification."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Show several examples to establish the expected labels.
prompt = """
Classify each review as Positive, Negative, or Neutral. Return only the label.

Review: "The delivery was quick and the product works perfectly."
Label: Positive

Review: "The item arrived broken and support did not reply."
Label: Negative

Review: "It is an ordinary notebook with 100 pages."
Label: Neutral

Review: "I love how easy this app is to use."
Label: Positive

Review: "The package was late, but the product is fine."
Label:
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
