import requests

from utils.config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN
)

def send_message(phone, message):

    url = (
        f"https://api.z-api.io/instances/"
        f"{ZAPI_INSTANCE_ID}/token/"
        f"{ZAPI_TOKEN}/send-text"
    )

    payload = {
        "phone": phone,
        "message": message
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }