import requests

import os

TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

r = requests.get(
    "https://api.github.com/user",
    headers=headers
)

print(r.status_code)
print(r.json())