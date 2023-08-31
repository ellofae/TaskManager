from database.models_extensions import BaseModelExtended

class TokenResponse(BaseModelExtended):
    access_token: str
    expiry: str