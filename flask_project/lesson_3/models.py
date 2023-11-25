from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
In SQLAlchemy, declarative base classes are used to define database models 
in an object-oriented manner.
"""
Base = declarative_base()


class Puppy(Base):
    __tablename__ = 'puppy'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
