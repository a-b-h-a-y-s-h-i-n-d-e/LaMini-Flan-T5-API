# API Endpoint which runs LaMini-Flan-T5-248M model

## Run locally
-> Run the Uvicorn server
```
uvicorn main:app --reload
```  

-> Post request to an endpoint
```
curl -X POST "http://127.0.0.1:8000/generate/" -H "Content-Type: application/json" -d '{"prompt": "what is rostering"}'
```
