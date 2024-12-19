import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_BOT_TOKEN")


def sendMessage(sender_id: int, message: str) -> None:
    url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage"

    payload = json.dumps({"chat_id": sender_id, "text": message})
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def sendPhoto(sender_id: int, photo_url: str, caption: str = "") -> None:
    url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendPhoto"

    payload = json.dumps({"chat_id": sender_id, "photo": photo_url, "caption": caption})
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


# sendMessage(5937979358, "Hello, World!")
# sendPhoto(
#     5937979358,
#     "https://scontent.fdac31-1.fna.fbcdn.net/v/t39.30808-6/470187265_122131016966484139_6335967559565341825_n.jpg?stp=dst-jpg_s1080x2048_tt6&_nc_cat=106&ccb=1-7&_nc_sid=127cfc&_nc_ohc=zaZ1NbogjG0Q7kNvgF0ZSf3&_nc_oc=Adjpz5gBbiWFfWt8M1xrKVb-pVZ85Ni9MzreYmgLaiKmaAoTi_nGN6hIa8agwNeIxFA&_nc_zt=23&_nc_ht=scontent.fdac31-1.fna&_nc_gid=Af7BdlQGs7ufqkC7PIojZe-&oh=00_AYBsMh3yIYivolSrxze0-X6f-UAxjw619Trh_FWuCP1k6g&oe=6767670E",
#     "This is a photo of SudiYunus",
# )
