from fastapi import APIRouter
from database import Session, engine
from schema import SignUpModel
from models import User

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


session = Session(bind=engine)
@auth_router.get('/')
async def hello():
    return {"message": "Hello World"}

@auth_router.post('/signup')
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    


    