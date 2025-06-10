import sys
from model import get_model_response


def run(user_prompt, verbose=False):
    text, ptokens, rtokens = get_model_response(user_prompt)
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
