#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.place import Place, place_amenity

class Amenity(BaseModel):
    """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenities = relationship(
        'Place', secondary=place_amenity, back_populates='amenities')
