import os

import httpx
from dotenv import load_dotenv
from google import genai
from google.genai._gaos.lib.compat_errors import APITimeoutError
from google.genai.errors import ServerError

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=genai.types.HttpOptions(timeout=30_000)
)
FALLBACK_MODEL = os.getenv("GEMINI_FALLBACK_MODEL", "gemini-3.5-flash")


def get_completion(prompt, model="gemini-3.8-flash"):
    try:
        response = client.interactions.create(model=model, input=prompt)
    except (ServerError, APITimeoutError, httpx.TimeoutException) as error:
        if (isinstance(error, ServerError) and error.code not in (503, 504)) or model == FALLBACK_MODEL:
            raise
        response = client.interactions.create(
            model=FALLBACK_MODEL,
            input=prompt
        )
    return response.output_text