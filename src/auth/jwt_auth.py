import jwt
import datetime

from decouple import config

def jwt_encode(user_id: int) -> (str, str):
    expiry = datetime.datetime.now() + datetime.timedelta(minutes=30)
    expiry_str = expiry.isoformat()

    payload = {
        "state": "access_token",
        "user_id": user_id,
        "expiry": expiry_str
    }

    encoded_jwt = jwt.encode(payload, config('JWT_SECRET_KEY'), algorithm=config('ENCODING_ALGORITHM'))
    return encoded_jwt, expiry.strftime("%Y-%m-%d %H:%M:%S")

def parse_jwt_token(token: str) -> dict:
    try:
        decoded_jwt = jwt.decode(token, config('JWT_SECRET_KEY'), algorithms=config('ENCODING_ALGORITHM'))
        return decoded_jwt
    except jwt.ExpiredSignatureError:
        raise ValueError("JWT token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid JWT token")
    except Exception as e:
        raise ValueError(f"Error decoding JWT token: {str(e)}")