import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def get_agent_response(prompt, model="gemini-2.0-flash-001"):
    response = client.models.generate_content(model=model, contents=prompt)
    return (
        response.text,
        response.usage_metadata.prompt_token_count,
        response.usage_metadata.candidates_token_count,
    )


text, ptokens, rtokens = get_agent_response("Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

print(text)
print(f"Prompt tokens: {ptokens}")
print(f"Response tokens: {rtokens}")
