from sqlmodel import SQLModel, Field
from datetime import datetime


class User(SQLModel, table=True):
    id: int | None = None
    username: str
    email: str
    password: str
    created_at: datetime  = Field(default_factory=datetime.now)
    