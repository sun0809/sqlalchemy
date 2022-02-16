from sqlalchemy import (create_engine, Column, 
String, Integer)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create engine and make files 
# pets.db : database / set where the database is going to be
engine = create_engine('sqlite:///pets.db',echo=False)
Session = sessionmaker(bind = engine)  # tying the session to our engine
session = Session()  # session class
Base = declarative_base()  
# reason for the capitalize ; related to a CLASS


class Pet(Base):
    __tablename__ = 'pets' # table inside of pets.db is 'pets'

    id = Column(Integer, primary_key=True)  # set it as primary key 
    name = Column(String)
    age = Column(Integer)
    pet_type = Column(String)

    def __repr__(self):
        return f'{self.id} | {self.name} {self.age} {self.pet_type}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
