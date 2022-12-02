import openai
from openai import InvalidRequestError

from subprocess import check_output, STDOUT, CalledProcessError
import os

import time


def write_to_file(text, file_path):
    """
    Writes passed text to file at location
    :param text: text to be written to file
    :param file_path: Relative or absolute path of file to be written
    :return:
    """
    with open(file_path, "w") as f:
        f.write(text)
    return True


def read_from_file(file_path) -> str:
    """
    Read file at given location and return text
    :param file_path: path of file to read
    :return:
    """
    with open(file_path) as f:
        return f.read()


def get_response_completion(prompt, model="code-davinci-002", temperature=0, max_tokens=300, retry=True,
                            **wargs) -> dict or None:
    """
    Returns result returned from OpenAI api
    Sample usage
    get_response("# program to return the nth fibbonacci number ")
    :param prompt: Prompt to be sent to openai model
    :param model: model to be used, check openai documentation on available models
    :param temperature: temperature argument, defaults to 0
    :param max_tokens: max number of tokens to be generated, defaults to 100
    :param retry: to retry again, if it fails once
    :param wargs: other arguments
    :return: response returned from API
    """
    try:
        response = openai.Completion.create(model=model,
                                            prompt=prompt, temperature=temperature, max_tokens=max_tokens, **wargs)
    except InvalidRequestError as ie:
        time.sleep(5)
        print(ie)
        if retry:
            return get_response_completion(prompt, model=model, temperature=temperature, max_tokens=max_tokens,
                                           retry=False, **wargs)
        return None
    except Exception as e:
        print(e)
        return None
    return response


def get_response_edit(inp, instruction, model="code-davinci-edit-001", temperature=0, retry=True,
                      **wargs) -> dict or None:
    """
    Sample usage
    get_response_edit(inp="def Fibonacci(n):\
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2
    print(Fibonacci(9))",
                 instruction="fix the error message "+result['error'].decode("utf-8")
                 )
    :param inp: input text on which instruction is to be performed
    :param instruction: input prompt to be done on input to modify them
    :param model: model to be used, check openai documentation on available models
    :param temperature: temperature argument, defaults to 0
    :param retry: to retry again, if it fails once
    :param wargs: other arguments
    :return:
    """
    try:
        response = openai.Edit.create(
            model=model,
            input=inp,
            instruction=instruction,
            **wargs
        )
    except InvalidRequestError as ie:
        time.sleep(10)
        print(ie)
        if retry:
            get_response_edit(inp, instruction, model, retry=False, temperature=temperature, **wargs)
        return None

    except Exception as e:
        print(e)
        return None

    return response

def get_code_edit(args, file_path="out_edit/sample.py"):
    """
    use OpenAPI to fetch the code from the file and captures instruction 
    from argument and then corrects the code until the output is correct

    :param prompt: text prompt to be sent to model
    :param file_path: location of file to write the result
    :param max_edit_count: number of retries to count
    :return:
    # """
    print("you have arrived edit method")
    prompt = " ".join(args.prompt)
    temp_file = "out_edit/temp"
    counter = 1
    max_edit_count = args.max_edit_count

    f = open(args.starter_code, "r")
    fdata = f.read()
    f.close()
    response = get_response_edit( inp = fdata ,instruction=prompt , temperature=args.temperature)
    if response is None:
        raise Exception("Failed to fetch result from API try again")

    print(response['choices'][0]['text'])
    write_to_file(response['choices'][0]['text'], file_path)
    write_to_file(response['choices'][0]['text'], temp_file + f"_{counter}.py")

    working, result = test_code(file_path)
    while not working and counter < max_edit_count:
        print(f"Correction attempt:{counter}")
        counter += 1
        response = get_response_edit(inp=response['choices'][0]['text'],
                                     instruction="\nfix the error message " + result['error']
                                     )
        if response is None:
            raise Exception("Failed to fetch result from API try again")
        write_to_file(response['choices'][0]['text'], file_path)
        write_to_file(response['choices'][0]['text'], temp_file + f"_{counter}.py")
        working, result = test_code(file_path)
    if working:
        print("Final result:")
        print(f"Program to :{prompt}")
        print('#' * 10)
        print(read_from_file(file_path))
        print('#' * 10)
    return


def get_code(args, file_path="out/sample1.py"):
    """
    use OpenAPI to fetch the code until it runs without errors
    :param prompt: text prompt to be sent to model
    :param file_path: location of file to write the result
    :param max_edit_count: number of retries to count
    :return:
    """
    prompt = " ".join(args.prompt)
    max_edit_count = args.max_edit_count

    temp_file = "out/temp"
    counter = 1
    response = get_response_completion(prompt, temperature=args.temperature, max_tokens=args.max_tokens)
    if response is None:
        raise Exception("Failed to fetch result from API try again")
    print(response['choices'][0]['text'])
    write_to_file(response['choices'][0]['text'], file_path)
    write_to_file(response['choices'][0]['text'], temp_file + f"_{counter}.py")

    working, result = test_code(file_path)
    while not working and counter < max_edit_count:
        print(f"Correction attempt:{counter}")
        counter += 1
        response = get_response_edit(inp=response['choices'][0]['text'],
                                     instruction="\nfix the error message " + result['error']
                                     )
        if response is None:
            raise Exception("Failed to fetch result from API try again")
        write_to_file(response['choices'][0]['text'], file_path)
        write_to_file(response['choices'][0]['text'], temp_file + f"_{counter}.py")
        working, result = test_code(file_path)
    if working:
        print("Final result:")
        print(f"Program to :{prompt}")
        print('#' * 10)
        print(read_from_file(file_path))
        print('#' * 10)
    return


def test_code(file_path):
    """
    Runs the code which is at given location
    :param file_path: path of file to run via python
    :return: Bool, Dictionary
    """
    result = {}
    working = True
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"this path doesn't exist: {file_path}")
    try:
        output = check_output(['python', file_path], stderr=STDOUT)
        result['out'] = output.decode("utf-8")
    except CalledProcessError as exc:
        print(exc.output.decode("utf-8"))
        result['error'] = exc.output.decode("utf-8")
        working = False
    else:
        print(result['out'])
    return working, result
