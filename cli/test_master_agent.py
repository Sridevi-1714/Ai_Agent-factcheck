import requests

router_url = "http://localhost:8080/agent/master_agent"

user_input = {
    "statement": input("Enter a statement to analyze: ")
}

print(f"Sending input: {user_input}")
response = requests.post(router_url, json=user_input)

if response.status_code == 200:
    print("✅ Response from master agent:")
    print(response.text)
else:
    print(f" Error: {response.status_code} - {response.text}")
