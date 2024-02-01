from decimal import Decimal
from sqlmodel import SQLModel, Field
from typing import Optional, Union

class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Union[str, None]
    price: Union[Decimal, None]
    launch: Union[str, None]