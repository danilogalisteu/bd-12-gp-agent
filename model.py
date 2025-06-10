import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from schemas import available_functions


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def get_model_response(user_prompt, model="gemini-2.0-flash-001"):
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    return client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )
