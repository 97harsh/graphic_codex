import openai
from config import get_config
import os,sys
from util import get_code
import argparse


def main(args):
    config = get_config()
    openai.api_key = config['API Key']
    get_code(" ".join(args.prompt))
    
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'Text to code',
                    description = 'Given a prompt -> create a code calling codex api')

    parser.add_argument('-p', dest="prompt", required=True, default= None, nargs="+",  help="Enter the prompt" )
    args = parser.parse_args()

    print( "Prompt: {} ".format(" ".join(args.prompt)))
    main(args)
