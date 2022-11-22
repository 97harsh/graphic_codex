import openai
from config import get_config
import os,sys
from util import get_code
import argparse


def main(args):
    config = get_config()
    openai.api_key = config['API Key']
    get_code(args)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'Text to code',
                    description = 'Given a prompt -> create a code calling codex api')

    parser.add_argument('-p', dest="prompt", required=True, default= None, nargs="+",  help="Enter the Prompt" )
    parser.add_argument('-t', dest="temperature", required=False,type=float, default=0,  help="Enter the temperature" )
    parser.add_argument('-ec', dest="max_edit_count", required=False,type=int, default=5,  help="Enter the Max edit count")
    parser.add_argument('-tok', dest="max_tokens", required=False,type=int, default=300, help="Enter the Max tokens count" )

    args = parser.parse_args()
    print(args)
    main(args)
