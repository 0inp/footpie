from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class LeagueModel(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    startYear = Column(Integer)
    endYear = Column(Integer)
    numberOfMatchDays = Column(Integer)

    country = relationship("Country", back_populates="leagues")
    # games = relationship("Game", back_populates="league")
    # clubs = relationship("Club", back_populates="league")
