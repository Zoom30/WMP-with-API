from decimal import Decimal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.data_database import DBDataAccess
from mangum import Mangum
from src.data_user import UserDataAccess

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/set_initial_details")
def set_initial_details(weight: Decimal, height: Decimal):
    data = DBDataAccess()
    return data.set_initial_details(weight, height)

@app.get("/initial_details")
def get_initial_details():
    data = DBDataAccess()
    items = data.get_initial_details().get('Items')
    return items

@app.post("/sign_up")
def sign_up(user_name: str, password: str, email: str):
    data = UserDataAccess()
    return data.sign_up(user_name, password, email)

@app.post("/sign_in")
def sign_in(email: str, password: str):
    data = UserDataAccess()
    return data.sign_in(email, password)

handler = Mangum(app)
