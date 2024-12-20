from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+pymysql://root:password@127.0.0.1:3306/banking"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
