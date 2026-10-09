# Prompt Engineering Practice

A beginner-friendly collection of runnable examples, short topic notes, and practical assignments for learning prompt engineering.

## Topics covered

1. Zero-shot prompting
2. One-shot prompting
3. Few-shot prompting
4. Multi-shot prompting
5. Chain-of-thought prompting
6. Zero-shot chain-of-thought
7. System, user, and assistant roles
8. Prompt structuring basics
9. Prompt reuse and versioning
10. JSON prompting and structured outputs
11. Prompt design patterns
12. Prompt tuning vs. instruction tuning

## Setup

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and set `GEMINI_API_KEY` to your Google Gemini API key. Do not commit the `.env` file.

The examples use the shared `helper.py` module, which sends prompts to Gemini. Calls require internet access and a valid API key.

## Run examples

From the project root, run an example with:

```powershell
python examples\01_zero_shot.py
```

Replace `01_zero_shot.py` with any of the other example filenames. The JSON example also parses the model's response with `json.loads()`, so invalid JSON is reported as an error rather than silently accepted.

## Folder structure

```text
.
|-- assignments/   # Short practical tasks and evaluation rules
|-- examples/      # Runnable Python prompt demonstrations
|-- prompts/       # Beginner-friendly topic notes
|-- helper.py      # Shared Gemini completion helper
|-- requirements.txt
|-- .env.example   # Environment-variable template
```