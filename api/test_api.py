import threading, time, warnings, sys, os

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import uvicorn
import requests
from api.search_api import app

HOST = "127.0.0.1"
PORT = 8543


def start_server():
    uvicorn.run(app, host=HOST, port=PORT, log_level="warning")


t = threading.Thread(target=start_server, daemon=True)
t.start()
time.sleep(4)

# Health check
r = requests.get(f"http://{HOST}:{PORT}/health")
print("Health:", r.status_code, r.json())

# Search by text
r = requests.post(
    f"http://{HOST}:{PORT}/search/text",
    json={"query": "How do I configure vector search?", "limit": 3},
)
print("Search status:", r.status_code)
data = r.json()
print("Response:", data)
