from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from juggler import Juggler

# Creating engine, table and Session class
engine = create_engine('sqlite:///jugglers.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Creating sample data objects
juggler1 = Juggler(name="Ian Stewart", country="Canada", catches=94)
juggler2 = Juggler(name="Aaron Gregg", country="Canada", catches=88)
juggler3 = Juggler(name="Chad Taylor", country="USA", catches=78)

# Adding sample objects to table
session = Session()
session.add_all([juggler1, juggler2, juggler3])
session.commit()
session.close()

# Get name, country, and catches from user and adds data to db
def add_juggler(name, country, catches):
    add_session = Session()
    new_juggler = Juggler(name=name, country=country, catches=catches)
    add_session.add(new_juggler)
    add_session.commit()
    add_session.close()


# Get juggler's name from the user, removes them from db
def remove_juggler(name):
    delete_session = Session()
    for juggler in delete_session.query(Juggler).filter_by(name=name):
        delete_session.delete(juggler)
    delete_session.commit()
    delete_session.close()


# Print contents of jugglers table
def show_all():
    view_session = Session()
    for juggler in view_session.query(Juggler):
        print(juggler)
    view_session.close()


# Edits a juggler's number of catches
def edit(name, catches):
    edit_session = Session()
    for juggler in edit_session.query(Juggler).filter_by(name=name):
        juggler.catches = catches
    edit_session.commit()
    edit_session.close()