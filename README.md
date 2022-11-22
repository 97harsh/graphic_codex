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

Prompting the program<br>
```python src/main.py "<PROMPT>"```
<br>eg:
```python src/main.py "program to print 7 rows of pascals triangle in python"```

