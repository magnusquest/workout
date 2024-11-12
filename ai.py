from dotenv import load_dotenv
load_dotenv()

from langflow.load import run_flow_from_json

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




def main():
  output = ask_ai("How many meals should I be eating daily and how many calories each?", "Male, 28, 5'11, 180lbs")
  print(output)
