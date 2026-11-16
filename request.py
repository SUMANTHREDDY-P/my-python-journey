import json

with open(".venv/json load and dump exercise/agent.json", "r") as config_file:
    config = json.load(config_file)

new_topics = [
    {
        "topic": "LangChain & LlamaIndex",
        "status": "learning"
    },
    {
        "topic": "Docker & Containerization",
        "status": "not started"
    }
]
config.extend(new_topics)

with open(".venv/json load and dump exercise/agent.json", "w") as config_file:
    json.dump(config, config_file , indent=4)