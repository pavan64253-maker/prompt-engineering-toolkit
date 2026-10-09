"""
Module 01 — Prompting Guidelines
Example: Zero-shot prompting
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Generate 10 simple business ideas for beginners. Keep each idea short, practical, and easy to understand.
"""
response = get_completion(prompt)
print("Prompt:")
print("-" * 50)
print(prompt)
print("\nResponse:")
print("-" * 50)
print(response)