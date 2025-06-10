import sys

from calls import call_function
from model import get_model_response


def run(user_prompt, verbose=False):
    response = get_model_response(user_prompt)

    if response.text:
        print(response.text)

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
 
    if response.function_calls:
        for call in response.function_calls:
            result = call_function(call, "calculator", verbose=verbose)
            try:
                response = result.parts[0].function_response.response
                if verbose:
                    print(f"-> {response}")
            except Exception as e:
                raise e


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py '<prompt>'")
        sys.exit(1)

    verbose = "--verbose" in sys.argv[1:]
    if verbose:
        sys.argv.remove("--verbose")
    run(sys.argv[1], verbose=verbose)
