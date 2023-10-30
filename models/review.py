<<<<<<< HEAD
#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
=======
#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
>>>>>>> d2bcc03fe412038f3218b5eb2721eb73340255d1
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
<<<<<<< HEAD
    """Representation of Review """
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
=======
    """This is the class for Review
    Attributes:
        __tablename__: table name
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
>>>>>>> d2bcc03fe412038f3218b5eb2721eb73340255d1
