import openai
from config import get_config
import os,sys
from util import get_code
from util import get_code_edit
import argparse
import os


def main(args):
    config = get_config()
    openai.api_key = config['API Key']
    if args.mode=="gen":
        get_code(args)
    if args.mode=="edit":
        get_code_edit(args)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'Text to code',
                    description = 'Given a prompt -> create/edit a code calling codex api')

    parser.add_argument('-m', dest="mode", required=True, default=None, choices=['edit','gen']   ,help="Enter the mode to operate -> either generate or edit")
    parser.add_argument('-p', dest="prompt", required=True, default= None, nargs="+",  help="Enter the Prompt" )
    parser.add_argument('-t', dest="temperature", required=False,type=float, default=0,  help="Enter the temperature" )
    parser.add_argument('-ec', dest="max_edit_count", required=False,type=int, default=5,  help="Enter the Max edit count")
    parser.add_argument('-tok', dest="max_tokens", required=False,type=int, default=300, help="Enter the Max tokens count" )
    parser.add_argument('-sc', dest="starter_code", required=False, default=None,  help="Enter the file location to edit")
    
    args = parser.parse_args()

    if args.prompt is None:
        print("Please provide the prompt")
        sys.exit()

    if args.mode == "edit":
        if args.starter_code is None:
            print("Please enter the location to starter code in edit mode")
            sys.exit()
        if not os.path.exists(args.starter_code):
            print("FILE: {} not present".format(args.starter_code))
            sys.exit()


    print(args)
    main(args)
