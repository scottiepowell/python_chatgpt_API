import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="This is a prompt for openai API")
args = parser.parser_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "osk-B0MTAZZhSv2SVLu8XrrnT3BlbkFJxPPE72ktBZzB4Bzq4kYZ"

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
    print(response.json()["choices"][0])
else:
    print(f"Request failed with status code {str(response.status_code)}")

