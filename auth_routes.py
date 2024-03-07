from fastapi import APIRouter,status,Depends
from database import Session, engine
from schema import SignUpModel,LoginModel
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


session = Session(bind=engine)
@auth_router.get('/')
async def hello():
    return {"message": "Hello World"}

@auth_router.post('/signup',
    status_code=201)
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()

    if db_email is not None:
        raise HTTPException(status_code=400, detail="Email already exists")

    db_username = session.query(User).filter(User.email == user.username).first()

    if db_email is not None:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = User(
        username = user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_active = user.is_active,
        is_staff = user.is_staff
    )

    session.add(new_user)

    session.commit()

    return new_user

#LOGIN

auth_router.post('/login'):
async def login(user:LoginModel,Authorize:AuthJWT=Depends()):
    db_user=session.query(User).filter(User.username==user.username).first()

    if db_user and check_password_hash(db_user.password,user.password):
        access_token=Authorize.create_access_token(subject=db_user.username)
        refresh_token=Authorize.create_refresh_token(subject=db_user.username)


