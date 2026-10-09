"""Example: requesting JSON and parsing the result."""

import json
import sys
from pathlib import Path

# Allow importing the shared helper from the project root.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Request a strict JSON object with predictable fields.
prompt = """
Suggest one beginner-friendly business idea.
Return only a valid JSON object with exactly these keys:
"name" (string), "audience" (string), and "first_step" (string).
Do not include Markdown fences or any text outside the JSON object.
"""

# Get the model response and parse it as JSON.
response = get_completion(prompt)
idea = json.loads(response)

# Print the original response and the parsed structure.
print("PROMPT:")
print("-" * 50)
print(prompt)
print("\nRESPONSE:")
print("-" * 50)
print(response)
print("\nPARSED JSON:")
print("-" * 50)
print(json.dumps(idea, indent=2, ensure_ascii=False))
