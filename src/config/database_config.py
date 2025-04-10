from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
engine = create_engine(
    "mysql+pymysql://root:carlos15@127.0.0.1:3306/credit-plus",
    echo=True,
)

Session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
