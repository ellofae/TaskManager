# TaskManager

## .env example
    DATABASE_USER=postgres
    DATABASE_PASSWORD=example
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    DATABASE_NAME=db_name

    ACCESS_TOKEN_EXPIRY_MINUTES=30

    ADMIN_PASSWORD=secret123
    JWT_SECRET_KEY=secret
    REFRESH_TOKEN_LENGTH = 128
    ENCODING_ALGORITHM=HS256

## Routers

    Authentication:

    POST '/authentication'
    POST '/authentication/login'

____

    Refresh token:

    POST '/refresh'

___
    Company:

    GET '/companies'
    GET '/companies/{company_id}'
    POST '/companies'
___
    Task:
    
    GET '/tasks'
    GET '/tasks/{task_id}'
    POST '/tasks'
    PATCH '/tasks/{task_id}'
    DELETE '/tasks/{task_id}'
