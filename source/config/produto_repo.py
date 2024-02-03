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
        return True
    
    @staticmethod
    def put_product(id_item, product, tabela):
        with Session(engine) as session:
            statement = select(tabela).where(tabela.id == id_item)
            result = session.exec(statement)
            game = result.one()

            if  product.name != None:
                game.name = product.name
            if product.price != None:
                game.price = product.price
            if product.launch != None:
                game.launch = product.launch
            session.add(game)
            session.commit()
            session.refresh(game)
        
        return True
    
    @staticmethod
    def delete_product(id_item, tabela):
        with Session(engine) as session:
            statement = select(tabela).where(tabela.id == id_item)
            result = session.exec(statement)
            game = result.one()
            session.delete(game)
            session.commit()
        