#!/usr/bin/python3
<<<<<<< HEAD
"""
Contains the class DBStorage
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Retrieve one object
        """
        if cls not in classes.values():
            return None

        total = models.storage.all(cls)
        for value in total.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        total_class = classes.values()

        if not cls:
            count = 0
            for clas in total_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
=======
"""This is the db storage class for AirBnB"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ as env


class DBStorage:
    """This class serializes instances for database storage
    Attributes:
        __engine: engin to connect db
        __session: session to interact with db
        __clsdict: dictionary of all classes
    """
    __engine = None
    __session = None
    __clsdict = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def __init__(self):
        """setup __engine
        """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                env['HBNB_MYSQL_USER'],
                env['HBNB_MYSQL_PWD'],
                env['HBNB_MYSQL_HOST'],
                env['HBNB_MYSQL_DB']
            ), pool_pre_ping=True
        )
        if env.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query for objects depend on the class
        Arguments:
            cls: class to query
        """
        d = {}
        cls = cls if not isinstance(cls, str) else self.__clsdict.get(cls)
        if cls:
            for obj in self.__session.query(cls):
                d["{}.{}".format(
                    cls.__name__, obj.id
                    )] = obj
            return (d)
        for k, cls in self.__clsdict.items():
            for obj in self.__session.query(cls):
                d["{}.{}".format(cls.__name__, obj.id)] = obj
        return (d)

    def new(self, obj):
        """add an object to current db session
        Arguments:
            obj: object to add
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from current db session
        Arguments:
            obj: object to delete
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=True)
        self.__session = scoped_session(factory)()

    def close(self):
        """remove current session and roll back all unsaved transactions
        """
        if self.__session:
            self.__session.close()
>>>>>>> d2bcc03fe412038f3218b5eb2721eb73340255d1
