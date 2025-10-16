# main.py
import os
import uvicorn
from fastapi import FastAPI, HTTPException , status
from fastapi.responses import JSONResponse
import httpx
from datetime import datetime, timezone  

# create the fastapi application instance
app = FastAPI(title="Backend Wizards - Profile API")


# url of the external cat facts api that returns JSON-like response
cat_fact_url = 'https://catfact.ninja/fact'


@app.get("/")
async def root():
    '''Root endpoin - provide API information'''
    
    return {
        "message": "Backend Wizards Profile API",
        "endpoints": {"/me": "Get Profile with cat fact",
                      "/docs": "Interactive API documentation"}
    }

# define the GET endpoint /me
@app.get("/me") 
async def get_profile():  # async func allows calling external api without blocking the server
    
    fallback_fact = "Couldn't fetch a cat fact right now. Cats still rule though!"
    try:
        # this creates an asynchronous http client with a 5sec timeout for the request
        # using 'async with' ensures the client is closed when done
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(cat_fact_url)  # send a get request and wait for response
            response.raise_for_status()  # raise an exception if http status code is an error
            fact_data = response.json()  # parse the response body to a python dict (the cat fact api returns JSON)
            cat_fact = fact_data.get('fact', fallback_fact)  # extract 'fact' key; if missing, use fallback
    except Exception:
        # catches any error (network, timeout, etc.); on error we return the fallback message
        cat_fact = fallback_fact

    # building response 
    response_data = {
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
    return JSONResponse(content=response_data, status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
