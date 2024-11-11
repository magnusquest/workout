from langflow.load import run_flow_from_json
TWEAKS = {
  "TextInput-xzxNz": {
    "input_value": "question"
  },
  "TextInput-8YRVz": {
    "input_value": "profile"
  },
}

result = run_flow_from_json(flow="AskAI.json",
                            input_value="message",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=False, # False by default
                            tweaks=TWEAKS)
