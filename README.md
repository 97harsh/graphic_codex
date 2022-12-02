## Identify Adversarial Examples which Codex can understand but Dall-E cannot



Sources:
* https://spectrum.ieee.org/openai-dall-e-2
* https://arxiv.org/pdf/2204.13807.pdf
* https://www.aiweirdness.com/the-drawings-of-dall-e/

Program for code generation using openai, with correction

Add API key, generated from:https://beta.openai.com/account/api-keys in config file at ./config.json
{
  "API Key": "<OPENAI-API key>"
}

## Code Usage
```
python src/main.py -h

usage: Text to code [-h] -m {edit,gen} -p PROMPT [PROMPT ...] [-t TEMPERATURE]
                    [-ec MAX_EDIT_COUNT] [-tok MAX_TOKENS] [-sc STARTER_CODE]

Given a prompt -> create/edit a code calling codex api

optional arguments:
  -h, --help            show this help message and exit
  -m {edit,gen}         Enter the mode to operate -> either generate or edit
  -p PROMPT [PROMPT ...]
                        Enter the Prompt
  -t TEMPERATURE        Enter the temperature
  -ec MAX_EDIT_COUNT    Enter the Max edit count
  -tok MAX_TOKENS       Enter the Max tokens count
  -sc STARTER_CODE      Enter the file location to edit
```

### 1. Code Generation

Prompting the program<br>
```python src/main.py -m gen -p <prompt>```
<br>
Example:<br>
```python src/main.py -m gen -p program to print 7 rows of pascals triangle in python ```
<br>

The working code is written into ```out/sample1.py```

generated code:

```
def pascal(n):
    for i in range(n):
        for j in range(i+1):
            print(binomialCoeff(i,j),end=" ")
        print()

def binomialCoeff(n,k):
    res=1
    if(k>n-k):
        k=n-k
    for i in range(k):
        res=res*(n-i)
        res=res//(i+1)
    return res

n=7
pascal(n)
```
Result from running the generated code:
```
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
```
  
### 2. Modify existing code with Instruction

```python src/main.py -m edit -p <Instruction> -sc <file location to initial code>```
<br>
Example:<br>
```python src/main.py -m edit -p correct the code -sc path_to_py_file ```
<br>

The working code is written into ```out_edit/sample1.py``` 

 Input code from file <br>
  ```
  Print("Hello World ! )
  ```
  Corrected Code <br>
  ```
  Print("Hello World ! ")
  ```
  Output in out_edit/sample1.py <br>
  ```
  Hello World !
  ```

