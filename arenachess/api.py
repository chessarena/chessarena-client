import requests

BASE_URL = "http://45.151.30.77" 

def post_move(user_token, match_id, move):
    """Send move to server"""
    response = requests.post(f"{BASE_URL}/matches/{match_id}/move", 
        json={
            "user_token": user_token,
            "move": move
        }
    )
    return response.json()

def get_user_token(username, password):
    """Get user token from server"""
    response = requests.post(f"{BASE_URL}/v1/login/by_username",
        json={
            "username": username,
            "password": password
        }
    )
    return response.json().get("token")