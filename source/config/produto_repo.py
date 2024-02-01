from sqlmodel import SQLModel, create_engine, select, Session
from source.config.connect_db import engine

class ProdutoConfig():
    
    @staticmethod
    def get_products(table):
        with Session(engine) as session:
            statement = select(table)
            result = session.exec(statement).all()
        return result

    @staticmethod
    def get_product(id_item, table):
        with Session(engine) as session:
            try:
                statement = select(table).where(table.id == id_item)
                result = session.exec(statement)
                game = result.one()
            except:
                return 'Product not found'
        return game

    @staticmethod
    def post_product(product):
        with Session(engine) as session:
            session.add(product)
            session.commit()
        