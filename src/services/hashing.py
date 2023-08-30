import bcrypt

def password_hashing(password: str) -> str:
    password_bytes = password.encode('utf-8')
    random_chars = bcrypt.gensalt()
    
    hashed_password = bcrypt.hashpw(password_bytes, random_chars)
    return hashed_password.decode('utf-8')

def password_compare(password: str, hashed_password: str):
    password_bytes = password.encode('utf-8')
    hashed_password = hashed_password.encode('utf-8')
    
    if not bcrypt.checkpw(password_bytes, hashed_password):
        return False
    
    return True

    