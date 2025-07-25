from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from db.base import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True, nullable=False)
    content = Column(String, index=True, nullable=False)
    keywords = Column(String, index=True, nullable=True)
    created_at = Column(DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title}, content={self.content}, keywords={self.keywords}, created_at={self.created_at})>"
