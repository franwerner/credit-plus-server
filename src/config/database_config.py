from sqlmodel import create_engine, Session

engine = create_engine(
    "mysql+pymysql://root:carlos15@127.0.0.1:3306/credit-plus",
    echo=True,
)


def db_session():
    return Session(engine)
