#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.amenity import Amenity, place_amenity
from models.review import Review
from models import storage

class Place(BaseModel):
    """ Place class """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenities = relationship(
        'Amenity', secondary=place_amenity, back_populates='place_amenities', viewonly=False)

    reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')

    if storage_type == 'file':
        @property
        def amenities(self):
            return [amenity for amenity in models.storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
    else:
        amenity_ids = []
