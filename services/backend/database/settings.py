from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = 'postgresql://cactus:99936022MCmc@localhost:5432/task_tracker' # для локальной разработки

# URL_DATABASE = 'postgresql+psycopg2://cactus:rH1jdjGcVGEuKQ7wSFg20dqEjn7fXcGI@dpg-cnq6s0v79t8c7396mmo0-a.frankfurt-postgres.render.com/task2?sslmode=require'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()