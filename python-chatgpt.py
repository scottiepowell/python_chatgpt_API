import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="This is a prompt for openai API")
parser.add_argument("file_name", help="This is the file name")
args = parser.parser_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "Write python script to xxx. Provide only code, no text",
    "max_tokens": 100,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]
    with open("xxx", "w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code {str(response.status_code)}")

