from decimal import Decimal
from sqlmodel import SQLModel, Field
from typing import Optional

class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: Decimal
    launch: str