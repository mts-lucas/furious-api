from typing import Optional

from pydantic import BaseModel


class ItemExampleSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None