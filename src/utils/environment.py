import os

SERVICE_PORT = os.environ.get("SERVICE_PORT", 30001)
SERVICE_MODE = os.environ.get("SERVICE_MODE", "gpu")
ASSISTANT_HOST = os.environ.get("ASSISTANT_HOST", "localhost")
ASSISTANT_PORT = os.environ.get("ASSISTANT_PORT", 30002)
ASSISTANT_URL = f"{ASSISTANT_HOST}:{ASSISTANT_PORT}"