from langflow.load import run_flow_from_json
import requests
from typing import Optional
import os
from dotenv import load_dotenv
load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "6a3283a7-1730-4991-9f5a-e33ecb6d7ffb"
APPLICATION_TOKEN = os.getenv("LANGFLOW_TOKEN")

def ask_ai(profile, question):
  TWEAKS = {
    "TextInput-xzxNz": {
      "input_value": question
    },
    "TextInput-8YRVz": {
      "input_value": profile
    },
  }
  result = run_flow_from_json(flow="AskAI.json",
                input_value="message",
                session_id="", # provide a session id if you want to use session state
                fallback_to_env_vars=False, # False by default
                tweaks=TWEAKS)
  resultOutput = result[0].outputs[0].results["text"].data["text"]
  return resultOutput

def get_macros(profile : str, goals : str):
  TWEAKS = {
    "TextInput-bIqkj": {
      "input_value": goals
    },
    "TextInput-S25Cr": {
      "input_value": profile
    },
  }
  return run_flow("random", tweaks=TWEAKS, application_token=APPLICATION_TOKEN)

def run_flow(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:

    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/ball"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }

    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)

    return response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]


def main():
  #output = ask_ai("How many meals should I be eating daily and how many calories each?", "Male, 28, 5'11, 180lbs")
  output = get_macros("Male, 180lbs, 28yrs, active", "I want to lose 10 pounds")
  print(output)