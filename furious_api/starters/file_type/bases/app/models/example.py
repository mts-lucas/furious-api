
# apague esse arquivo ou renomeie, lembrando de apagar o import do models.main
from app.core.database import Base
from sqlalchemy import Column, Float, Integer, String


class ItemExample(Base):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    price = Column(Float)
    tax = Column(Float, nullable=True)