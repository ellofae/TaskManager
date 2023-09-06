# TaskManager
____

TaskManager is a RESTful API written in Python using the FastAPI framework and the SQLAlchemy ORM library. It implements the hexagonal architecture and the CQRS pattern. These architectural approaches ensure a flexible and scalable structure, while improving code cleanliness and modularity. TaskManager allows managing tasks and provides a user-friendly interface for interacting with them.

TaskManager API provides additional functionality that allows developers to integrate task creation and management directly into their applications or services. With the API, it is easy to create tasks, set priorities, due dates, and add subtasks for more detailed work breakdown.

One key feature of the API is the ability to assign users with different roles in the company to specific tasks. This allows for efficient responsibility distribution and workflow management.

## Ways to launch the api
____

* Docker: `./docker.sh` or `docker-compose up`
* Direct: `python src/run.py` (requirements.txt should be processed before)

## Configuration
_____
add the `.env` file:

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
