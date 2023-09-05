import secrets
import string

def generate_refresh_token(length: int) -> str:
    characters = string.ascii_letters + string.digits
    refresh_token = ''.join(secrets.choice(characters) for _ in range(length))
    return refresh_token