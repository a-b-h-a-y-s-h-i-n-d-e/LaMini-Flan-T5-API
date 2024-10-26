import languagemodels as lm
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import ssl
app = FastAPI()

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(
    certfile='/home/ubuntu/ssl_certs/fullchain.pem',
    keyfile='/home/ubuntu/ssl_certs/privkey.pem'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt : str

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Method: {request.method}, Path: {request.url.path}")
    response = await call_next(request)
    return response


@app.get('/')
def home():
    return {"msg" : "home"}

@app.get('/about')
def info():
    var = lm.config['instruct_model']
    return {"info" : var}

@app.post('/generate/')
def generate_response(request : PromptRequest):

    try:
        res = lm.do(request.prompt)
        return {"response": res}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

