<<<<<<< HEAD
#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
=======
#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.state import State
>>>>>>> d2bcc03fe412038f3218b5eb2721eb73340255d1
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
<<<<<<< HEAD
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
=======
    """This is the class for City
    Attributes:
        __tablename__: name of the table represented
        state_id: The state id
        name: input name
    """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="all, delete", backref="city")
>>>>>>> d2bcc03fe412038f3218b5eb2721eb73340255d1
