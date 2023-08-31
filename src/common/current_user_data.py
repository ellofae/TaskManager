from fastapi import Request

def get_current_user_id(request: Request) -> int:
    return request.state.user_id
