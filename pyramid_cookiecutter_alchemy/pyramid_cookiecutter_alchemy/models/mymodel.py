from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Entries(Base):
    __tablename__ = 'Journals'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    created = Column(Text)

