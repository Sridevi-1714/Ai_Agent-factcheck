# import requests

# router_url = "http://localhost:8080/agent/statement_checker_agent"

# user_input = {
#     "statement": "The Earth is flat and the moon landing was fake"
# }

# print(f"Sending input: {user_input}")
# response = requests.post(router_url, json=user_input)

# print("Response from agent:")
# print(response.text)

import requests

router_url = "http://localhost:8080/agent/statement_checker_agent"

user_input = {
    "statement": input("Enter a statement to check: ")
}

print(f"Sending input: {user_input}")
response = requests.post(router_url, json=user_input)

if response.status_code == 200:
    print(" Response from agent:")
    print(response.text)
else:
    print(f" Error: {response.status_code} - {response.text}")
