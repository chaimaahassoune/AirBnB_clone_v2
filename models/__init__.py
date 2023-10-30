#!/usr/bin/python3
<<<<<<< HEAD
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
=======
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ as env

if env.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
>>>>>>> d2bcc03fe412038f3218b5eb2721eb73340255d1
    storage = FileStorage()
storage.reload()
