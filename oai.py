import openai
import argparse
import os
import json

# read each line of the file into an array of dicts and return it
def load_history(file="chat_history.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# append the message to the array of dicts
def save_history(messages, file="chat_history.json"):
    with open(file, "w") as f:
        json.dump(messages, f)

def generate_text(prompt, model, temperature, max_tokens, history):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    
    messages = history.copy()
    messages.append({
        "role": "user",
        "content": prompt
    })

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].message

def main():
    try:
        with open('settings.json', 'r') as f:
            default_settings = json.load(f)
    except FileNotFoundError:
        default_settings = {}

    parser = argparse.ArgumentParser(description='OpenAI GPT API CLI')
    
    parser.add_argument('-p', '--prompt', type=str, default=default_settings.get('prompt', None), help='The prompt for the API')
    parser.add_argument('-m', '--model', type=str, default=default_settings.get('model', 'gpt-3.5-turbo'), help='The model to use')
    parser.add_argument('-t', '--temperature', type=float, default=default_settings.get('temperature', 0.7), help='The temperature setting for the API')
    parser.add_argument('-mt', '--max_tokens', type=int, default=default_settings.get('max_tokens', 150), help='The maximum number of tokens for the API response')
    parser.add_argument('-s', '--set', nargs=2, metavar=('setting', 'value'), help='Set and save a parameter. Usage: --set parameter value')
    parser.add_argument('-v', '--view', action='store_true', help='View current settings')
    
    args = parser.parse_args()
    
    if args.view:
        print(f"Current settings:\nModel: {args.model}\nTemperature: {args.temperature}\nMax Tokens: {args.max_tokens}")
        return
    
    if args.set:
        param, value = args.set
        default_settings[param] = value
        with open('settings.json', 'w') as f:
            json.dump(default_settings, f)
        print(f"Changed `{param}` to `{value}`")
        return
    
    if args.prompt:
        # load history from file into array of dicts
        history = load_history()
        result = generate_text(args.prompt, args.model, args.temperature, args.max_tokens, history=history)
        print("AI: ", result.content)
        # append the message to the array of dicts
        messages = history.copy()
        messages.append(result)
        save_history(messages)

if __name__ == "__main__":
    main()
