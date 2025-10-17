from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
import httpx
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Configuration
USER_EMAIL = "basseyelisha99@gmail.com"
USER_NAME = "Elisha Bassey"
USER_STACK = "Python/FastAPI"
CAT_FACT_API = "https://catfact.ninja/fact"
TIMEOUT = 5  # seconds


@app.get("/me")
async def get_profile():
    """
    Dynamic profile endpoint that returns user information and a random cat fact.
    """
    try:
        # Fetch cat fact from external API
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.get(CAT_FACT_API)
            response.raise_for_status()
            cat_data = response.json()
            cat_fact = cat_data.get("fact", "Unable to fetch cat fact")
    
    except httpx.TimeoutException:
        logger.error("Cat Facts API timeout")
        cat_fact = "The cat fact API timed out. Please try again."
    except httpx.HTTPError as e:
        logger.error(f"HTTP error fetching cat fact: {e}")
        cat_fact = "Unable to fetch cat fact at this moment."
    except Exception as e:
        logger.error(f"Unexpected error fetching cat fact: {e}")
        cat_fact = "An error occurred while fetching the cat fact."
    
    # Get current UTC time in ISO 8601 format
    current_timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    
    # Build response structure
    response_data = {
        "status": "success",
        "user": {
            "email": USER_EMAIL,
            "name": USER_NAME,
            "stack": USER_STACK
        },
        "timestamp": current_timestamp,
        "fact": cat_fact
    }
    
    logger.info(f"Profile request processed at {current_timestamp}")
    
    return JSONResponse(
        content=response_data,
        status_code=200,
        media_type="application/json"
    )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)