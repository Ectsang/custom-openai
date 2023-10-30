# Chat with OpenAI 🤖

## What is this?

A simple OpenAPI command line tool that lets you tweak your API parameters like `model`, `temperature`, and `max_tokens`.

## What do I need first?

1. A modern computer with an Internet connection.
2. Python 3.11.6 installed. If you don't have it, [click here](https://www.python.org/downloads/release/python-3116/) to download it.

## How do I set it up?

1. Download or clone this project from GitHub.
2. Open your computer's command line tool (like Terminal for Mac or Command Prompt for Windows).
3. Go to the folder where you downloaded this project.
4. (Optional) Create a virtual environment for this project. (If you don't know what this is, you can skip this step.
5. Set the `OPENAI_API_KEY` environment variable to your OpenAI API key. (If you don't have one, you can sign up for an OpenAI account and get one [here](https://platform.openai.com/account/api-keys). 
6. In yout Terminal (if you're on a Mac), type the following (replace `<your-api-key>` with your actual API key from OpenAI)
```
export OPENAI_API_KEY=<your-api-key> 
``` 
7. Install the required Python packages by typing `pip install -r requirements.txt` and pressing Enter.
8. Type `python oai.py -p "Hi there!"` and press Enter.
9. (Optional) if typing `python oai.py -p` you can use an alias like `oai` instead of `python oai.py`. To do this, type `alias oai="python $(pwd)/oai.py"` and press Enter.

Now you can chat with your computer friend!

## How do I use it?

You can ask the computer program questions or have it write stories for you. Just type:

```bash
python oai.py -p "Tell me a joke"
```

And it will tell you a joke! 😄 

The `-p` is a shortcut for `--prompt`. There is a whole world of Prompt Engineering that you can explore. 

There are other parameters you can use to customize your experience. See [below](#advanced-usage) for more details. 

## Advanced usage

You can view all the parameters by typing:

```bash
python oai.py -h
```

And it will show you all the parameters you can use.

```
python oai.py -h
usage: oai.py [-h] [-p PROMPT] [-m MODEL] [-t TEMPERATURE] [-mt MAX_TOKENS] [-s setting value] [-v]

OpenAI GPT API CLI

options:
  -h, --help            show this help message and exit
  -p PROMPT, --prompt PROMPT
                        The prompt for the API
  -m MODEL, --model MODEL
                        The model to use
  -t TEMPERATURE, --temperature TEMPERATURE
                        The temperature setting for the API
  -mt MAX_TOKENS, --max_tokens MAX_TOKENS
                        The maximum number of tokens for the API response
  -s setting value, --set setting value
                        Set and save a parameter. Usage: --set parameter value
  -v, --view            View current settings
```

Any time you set a parameter, it will be saved for the next time you use the program. For instance, if you want to use the `--model` parameter, you can set it like this:

### Using the `--model` parameter
You can also set the `model` parameter. This is the model that the computer program will use to generate text. The default value is `gpt-3.5-turbo`. You can see a list of available models [here](https://platform.openai.com/docs/api-reference/completions/create#completions-create-model).

```bash
python oai.py -s model davinci
```
This command will set the model to `davinci`. The next time you run the program, it will use this value.

### Using the `--temperature` parameter
You can customize some of the parameters of your OpenAI API calls. For instance, if you're generating code and want more accuracy rather than creativity, you can set the `temperature` parameter to 0.0. If you want more creativity, you can set it to 1.0. The default value is 0.7.

```bash
python oai.py -s temperature 0.5
```
This command will set the temperature to 0.5. The next time you run the program, it will use this value.

### Using the `--max-tokens` parameter
You can also set the `max-tokens` parameter. This is the maximum number of tokens (words) that the computer program will generate. The default value is 150. The maximum tokens is dependent on which model you use.

```bash
python oai.py -s max_tokens 1024
```
This command will set the maximum number of tokens to 1024. The next time you run the program, it will use this value.

### Viewing the current settings
You can view the current settings by typing:

```bash
python oai.py -v
```

Or (if you've already used the `--set` parameter):

Look at the contents of the `settings.json` file in the project folder.


## Resetting Your Chat History
If you want to reset your chat history, you can delete the `chat_history.json` file in the project folder.

## Can I help make this better?
Yes, you can! If you know how to code, you can add new things to this project by forking this repository and submitting a pull request (PR). If you find a problem, you can tell us so we can fix it.

## Questions?
If you have any questions, you can raise an issue.
