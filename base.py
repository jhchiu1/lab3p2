from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///jugglers.db', echo=False)
Base = declarative_base()