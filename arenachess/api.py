import requests

BASE_URL = "https://arenachess.com"

def post_move(user_token, match_id, move):
    response = requests.post(f"{BASE_URL}/matches/{match_id}/move", json={
        "user_token": user_token,
        "move": move
    })
    return response.json()
