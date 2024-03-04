from database import Base, engine
from models import User, Choice

Base.metadata.create_all(bind=engine)
