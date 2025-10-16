# main.py
from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
import httpx
from datetime import datetime, timezone  

# create the fastapi application instance
app = FastAPI()

# url of the external cat facts api that returns JSON-like response
cat_api_url = 'https://catfact.ninja/fact'

# define the GET endpoint /me
@app.get("/me", response_class=JSONResponse)  # a registered func to handle the get request and respond in JSON content_type
async def get_profile():  # async func allows calling external api without blocking the server
    fallback_fact = "Couldn't fetch a cat fact right now. Cats still rule though!"
    try:
        # this creates an asynchronous http client with a 5sec timeout for the request
        # using 'async with' ensures the client is closed when done
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(cat_api_url)  # send a get request and wait for response
            resp.raise_for_status()  # raise an exception if http status code is an error
            fact_data = resp.json()  # parse the response body to a python dict (the cat fact api returns JSON)
            cat_fact = fact_data.get('fact', fallback_fact)  # extract 'fact' key; if missing, use fallback
    except Exception:
        # catches any error (network, timeout, etc.); on error we return the fallback message
        cat_fact = fallback_fact

    # building response payload in the required format
    payload = {
        'status': 'success',  # must always be "success" as per task
        'user': {
            'email': 'basseyelisha99@gmail.com',
            'name': 'Elish Bassey',
            'stack': 'Python / FastAPI'  
        },
        'timestamp': datetime.now(timezone.utc).isoformat(),  # current UTC time in ISO 8601 format
        'fact': cat_fact  # dynamic cat fact from external API (or fallback)
    }

    # return JSONResponse (ensures content-type: application/json)
    return JSONResponse(content=payload, status_code=status.HTTP_200_OK)
