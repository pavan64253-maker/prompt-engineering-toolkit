# System, user, and assistant roles

## What it means
Role-based prompts distinguish instructions about the assistant from the user's request and the assistant's reply.

## When to use it
Use roles to separate durable behavior guidance from the specific task in APIs that support message roles.

## Small example
System: “You are a concise writing coach.” User: “Suggest a reading habit.” Assistant: responds with a plan.

## Key takeaway
This project helper accepts one text prompt, so the example labels the roles in text rather than sending separate API message objects.
