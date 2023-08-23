#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='all, delete')
    else:
        name = ""
        state_id = ""

        __tablename__ = "cities"

        @property
        def places(self):
            """getter for places"""
            place_list = []
            all_places = models.storage.all(models.place.Place)
            for place in all_places.values():
                if place.city_id == self.id:
                    place_list.append(place)
            return place_list
