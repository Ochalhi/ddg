import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine(os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/postgres"), echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


# noinspection PyUnresolvedReferences
def init_db():
    import chatapp.models.User
    import chatapp.models.Message
    Base.metadata.create_all(bind=engine)
