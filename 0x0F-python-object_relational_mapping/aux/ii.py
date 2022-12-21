from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, create_engine, Column

db_url = "mysql+mysqldb://{}:{}@localhost/{}".format("root", "Yusuf-2706", "sqlalchemy")
engine = create_engine(db_url)
Base = declarative_base()
class Network(Base):
    __tablename__ = "network"
    network_id = Column(Integer), primary_key=True)
    name = Column(String(), nullable=False)

Base.metadata.create_all(engine)
