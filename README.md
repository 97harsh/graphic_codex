## Identify Adversarial Examples which Codex can understand but Dall-E cannot



Sources:
* https://spectrum.ieee.org/openai-dall-e-2
* https://arxiv.org/pdf/2204.13807.pdf
* https://www.aiweirdness.com/the-drawings-of-dall-e/

Program for code generation using openai, with correction

Add API key, generated from:https://beta.openai.com/account/api-keys in config file at ./config.json
<br>
{
  "API Key": "<OPENAI-API key>"
}

Prompting the program<br>
```python src/main.py "<PROMPT>"```
<br>eg:
```python src/main.py "program to print 7 rows of pascals triangle in python"```
<br>
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