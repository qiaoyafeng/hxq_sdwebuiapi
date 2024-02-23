from sqlalchemy import Column, Integer, String, TIMESTAMP, func

from db.database import Base


class Resource(Base):
    __tablename__ = "resource"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(1000))
    keyword = Column(String(200))
    info = Column(String(1000))
    create_time = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
