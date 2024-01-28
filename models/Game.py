from pydantic import BaseModel
from decimal import Decimal

class Game(BaseModel):
    name: str
    price: Decimal
    launch: str