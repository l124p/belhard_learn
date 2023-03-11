from typing import Any, Type, Sequence
from sqlalchemy import Column, INT, VARCHAR, ForeignKey, create_engine, select, Row, RowMapping
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, Session


class Base(DeclarativeBase):
    id = Column('id', INT, primary_key=True, unique=True)

    db_engine = create_engine("postgresql://postgres:postgres@localhost/db")
    db_session = sessionmaker(bind=db_engine)

    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with Base.db_session() as session:
                return func(*args, **kwargs, session=session)

        return wrapper

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    @create_session
    def save(self, session: Session = None) -> None:
        session.add(self)
        session.commit()
        session.refresh(self)

    @create_session
    def delete(self, session: Session = None) -> None:
        session.delete(self)
        session.commit()

    @classmethod
    @create_session
    def get(cls, id: Any, session: Session = None) -> Type["Base"]:
        return session.get(cls, id)

    @classmethod
    @create_session
    def select(
            cls,
            *args,
            order_by: Any = 'id',
            limit: int = None,
            offset: int = None,
            session: Session = None
    ) -> Sequence[Row | RowMapping | Any]:
        return session.scalars(
            select(cls)
            .order_by(order_by)
            .limit(limit)
            .offset(offset)
            .filter(*args)
        ).all()

    def dict(self) -> dict:
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


class Statuses(Base):
    name = Column(VARCHAR(10), unique=True)


class Orders(Base):
    user_id = Column('user_id', INT, ForeignKey('users.id', ondelete='CASCADE'))
    status_id = Column('status_id', INT, ForeignKey('statuses.id', ondelete='CASCADE'))


class OrdersItems(Base):
    order_id = Column(INT, ForeignKey('orders.id', ondelete='CASCADE'))
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'))


class Users(Base):
    name = Column(VARCHAR(24))
    email = Column(VARCHAR(24), unique=True)


class Products(Base):
    title = Column(VARCHAR(36))
    description = Column(VARCHAR(140))
    category_id = Column(INT, ForeignKey('categories.id', ondelete='Cascade'))


class Categories(Base):
    name = Column(VARCHAR(24), unique=True)
