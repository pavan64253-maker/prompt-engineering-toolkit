# JSON prompting and structured outputs

## What it means
Ask the model for data in a strict JSON structure so code can parse it.

## When to use it
Use it when an application needs named fields rather than free-form text.

## Small example
Request a JSON object with a business idea's name, audience, and first step, then parse it with `json.loads()`.

## Key takeaway
Specify exact keys and valid JSON, and handle parsing errors rather than assuming the response is valid.
