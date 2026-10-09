"""Example: applying multiple prompt design patterns to one input."""

import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

input_text = (
    "The customer says their desk lamp arrived late and the switch is broken. "
    "They would like a replacement before Monday."
)

# Apply four patterns to the same source text.
prompts = {
    "Classification": (
        f"Classify the main support category for this message as Delivery, "
        f"Damaged item, Billing, or Other. Return one label only.\n\n{input_text}"
    ),
    "Extraction": (
        f"Extract the issue, requested resolution, and deadline from this message. "
        f"Use three labeled lines and do not add assumptions.\n\n{input_text}"
    ),
    "Transformation": (
        f"Rewrite this message as a concise, polite support ticket while preserving "
        f"all facts.\n\n{input_text}"
    ),
    "Generation": (
        f"Draft a short, empathetic reply acknowledging the reported problem and "
        f"stating that the support team will check replacement options. Do not "
        f"promise a delivery date.\n\n{input_text}"
    ),
}

# Request and display a separate response for each pattern.
print("INPUT TEXT:")
print("-" * 50)
print(input_text)
for pattern, prompt in prompts.items():
    response = get_completion(prompt)
    print(f"\n{pattern.upper()} PROMPT:")
    print("-" * 50)
    print(prompt)
    print(f"\n{pattern.upper()} RESPONSE:")
    print("-" * 50)
    print(response)
