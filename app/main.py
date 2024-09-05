from uvicorn import run
from settings.config import app


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000, reload=True)
