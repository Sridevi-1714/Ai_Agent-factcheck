# import requests

# router_url = "http://localhost:8080/agent/fact_source_agent"

# user_input = {
#     "statement": "Is the Earth flat or did the moon landing actually happen?"
# }

# print(f"Sending input: {user_input}")
# response = requests.post(router_url, json=user_input)

# print("Response from agent:")
# print(response.text)

import requests

router_url = "http://localhost:8080/agent/fact_source_agent"

user_input = {
    "statement": input("Enter a statement to fact-check: ")
}

print(f"Sending input: {user_input}")
response = requests.post(router_url, json=user_input)

if response.status_code == 200:
    print(" Response from agent:")
    print(response.text)
else:
    print(f" Error: {response.status_code} - {response.text}")
