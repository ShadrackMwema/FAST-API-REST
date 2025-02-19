from fastapi import FastAPI
import uvicorn
from firebase_admin import credentials
from models import LoginSchema,SignUpSchema
import firebase_admin
import pyrebase
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request

#define fastAPI instance
#it uses asgi server


app = FastAPI(
    description="This is a simple App",
    title= "Simple FastAPI App",
    docs_url="/",#by default it is /docs url or swagger url
)

# routes

if not firebase_admin._apps:
    cred = credentials.Certificate("fastapi-26a9e-firebase-adminsdk-fbsvc-802e3ca86f.json")
    firebase_admin.initialize_app(cred)


async def create_an_account():
    pass
firebaseConfig = {
  "apiKey": "AIzaSyD5efBDsU1zlgNlZZIXdTD7aXtqmDdYwUA",
  "authDomain": "fastapi-26a9e.firebaseapp.com",
  "projectId": "fastapi-26a9e",
  "storageBucket": "fastapi-26a9e.firebasestorage.app",
  "messagingSenderId": "545588384510",
  "appId": "1:545588384510:web:f09209e760059e320f0baf",
  "measurementId": "G-6ZF51DKVMB",
  "databaseURL" : "SJCJK"
}
firebase = pyrebase.initialize_app(firebaseConfig)


@app.post('/signup')
async def create_an_account(user_data:SignUpSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = auth.create_user(
            email = email,
            password = password
        )

        return JSONResponse(content={"message" : f"User account created successfuly for user {user.uid}"},
                            status_code= 201
               )
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail= f"Account already created for the email {email}"
        )





@app.post('/login')
async def create_access_token(user_data:LoginSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = firebase.auth().sign_in_with_email_and_password(
            email = email,
            password = password
        )

        token = user['idToken']

        return JSONResponse(
            content={
                "token":token
            },status_code=200
        )

    except:
        raise HTTPException(
            status_code=400,detail="Invalid Credentials"
        )

@app.post('/ping')
async def validate_token(request:Request):
    headers = request.headers
    jwt = headers.get('authorization')

    user = auth.verify_id_token(jwt)

    return user["user_id"]

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)