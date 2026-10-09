"""Example: multi-shot support ticket tagging."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Use many examples to make the ticket-labeling pattern consistent.
prompt = """
Assign each support ticket exactly one label from:
Billing, Delivery, Technical, Account, or Returns.
Return only the label.

Ticket: "I was charged twice for my monthly plan."
Label: Billing
Ticket: "The tracking page has not updated in three days."
Label: Delivery
Ticket: "The app closes whenever I open the settings page."
Label: Technical
Ticket: "I need to change the email address on my profile."
Label: Account
Ticket: "Please tell me how to send back the shoes I ordered."
Label: Returns
Ticket: "My invoice includes a fee I do not recognize."
Label: Billing
Ticket: "The courier left my parcel at the wrong building."
Label: Delivery
Ticket: "I cannot reset my password because the link expired."
Label: Account

Ticket: "The headphones arrived, but one side has no sound."
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
