import openai
from config import get_config
import sys
from util import get_code


def main(prompt):
    config = get_config()
    openai.api_key = config['API Key']
    get_code(prompt)
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 1:
        prompt = "program to print hello world in python"
    else:
        prompt = sys.argv[1]
    main(prompt)
