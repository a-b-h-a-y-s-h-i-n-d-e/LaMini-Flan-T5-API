import languagemodels as lm
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#var = lm.config['instruct_model']
#print(var)

class PromptRequest(BaseModel):
    prompt : str

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
        return {"response", res}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

