import os
from dotenv import load_dotenv

load_dotenv()

FRONTEND_URL = os.getenv("Frontend_URL", "http://localhost:5173")

ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    FRONTEND_URL,
]