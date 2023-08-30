import sys

from uvicorn import run

if __name__ == "__main__":
    print("Starting the server...")
    sys.exit(run("main:app", host="0.0.0.0", port=5000, reload=True, access_log=True))