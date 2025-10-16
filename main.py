from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from datetime import datetime
import os

app = FastAPI()

@app.get("/me")
def get_profile():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "No cat fact available.")
    except Exception:
        cat_fact = "Could not fetch cat fact at the moment."

    result = {
        "status": "success",
        "user": {
            "email": "basseyelisha99@gmail.com",
            "name": "Elisha Bassey",
            "stack": "Python/django"
        },
        # ISO 8601 UTC timestamp
        "timestamp": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
        "fact": cat_fact
    }

    return JSONResponse(content=result)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
