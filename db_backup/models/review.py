#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = 'reviews'
    place_id = Column(String(60), nullable=False, ForeignKey(places.id))
    user_id = Column(String(60), nullable=False, ForeignKey(users.id))
    text = Column(String(1024), nullable=False)
