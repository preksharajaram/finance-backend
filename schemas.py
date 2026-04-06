from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: str
    role: str
    status: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


class TransactionBase(BaseModel):
    amount: float
    type: str
    category: str
    date: str
    description: Optional[str] = None


class TransactionCreate(TransactionBase):
    pass


class TransactionResponse(TransactionBase):
    id: int

    class Config:
        from_attributes = True