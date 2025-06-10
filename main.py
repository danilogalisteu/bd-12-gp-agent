import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def get_agent_response(prompt, model="gemini-2.0-flash-001"):
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    return (
        response.text,
        response.usage_metadata.prompt_token_count,
        response.usage_metadata.candidates_token_count,
    )


def run(user_prompt, verbose=False):
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    text, ptokens, rtokens = get_agent_response(messages)
    print(text)

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {ptokens}")
        print(f"Response tokens: {rtokens}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py '<prompt>'")
        sys.exit(1)

    verbose = "--verbose" in sys.argv[1:]
    if verbose:
        sys.argv.remove("--verbose")
    run(sys.argv[1], verbose=verbose)
