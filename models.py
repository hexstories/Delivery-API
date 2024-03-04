from database import Base
from sqlalchemy import Column, Integer, String, Boolean,Text,ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    orders = relationship("Choice", back_populates="user")


    def __repr__(self):
        return f"<User {self.username}>"
    

class Choice(Base):

    ORDER_STATUS = (
        ("Pending", "Pending"),
        ("IN-TRANSIT", "In-Transit"),
        ("Delivered", "Delivered"),

    )

    PIZZA_SIZES = (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
        ("Extra-Large", "Extra-Large"),
    )
    __tablename__ = "choices"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(ORDER_STATUS), default="Pending")
    pizza_size = Column(ChoiceType(PIZZA_SIZES), default="Small")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user=relationship("User", back_populates="orders")
    



    
    def __repr__(self):
        return f"<Choice {self.id}>"