from fastapi import FastAPI
import uvicorn

#define fastAPI instance
#it uses asgi server


app = FastAPI(
    description="This is a simple App",
    title= "Simple FastAPI App",
    docs_url="/",#by default it is /docs url or swagger url
)

# routes
@app.post("/signup")
async def create_an_account():
    pass

@app.post("/login")
async def create_access_token():
    pass

@app.post("/ping")
async def validate_token():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True) #reload=True will reload the server when changes are made in the code

