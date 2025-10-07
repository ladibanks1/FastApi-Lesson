from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase

# Local Database
DATABASE_URI = "postgresql://admin:*******@localhost:5432/postgres"

engine = create_engine(DATABASE_URI, echo=True)

session = sessionmaker(bind=engine)


def db_session():
    with session() as db_session:
        yield db_session


class Base(DeclarativeBase):
    def to_dict(
        self, include_relationship=True, exclude: list[any] | set | tuple = None
    ):
        exclude = exclude or set()
        result = {
            cols.key: getattr(self, cols.key)
            for cols in self.__table__.columns
            if cols.key not in exclude
        }

        if include_relationship:
            for key, relation in self.__mapper__.relationships.items():

                value = getattr(self, key)
                if value is None:
                    result[key] = None
                elif relation.uselist:
                    result[key] = {
                        item.to_dict() for item in value if item not in exclude
                    }
                else:
                    result[key] = value.to_dict()
        return result
