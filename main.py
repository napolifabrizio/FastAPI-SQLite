from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session, select
from models.Game import Game
from typing import Union
from decimal import Decimal

app = FastAPI()

engine = create_engine("sqlite:///database.sqlite")

SQLModel.metadata.create_all(engine)

@app.get('/')
def start():
    return 'Welcome to my API'

@app.get('/show_products')
def get_products():
    with Session(engine) as session:
        statement = select(Game)
        result = session.exec(statement).all()
    return result

@app.post('/insert_product')
def post_product(product: Game):
    with Session(engine) as session:
        session.add(product)
        session.commit()
    return 'The product has been inserted'

@app.put('/update_product/{id_item}')
def put_product(id_item: int, product: Game):
    with Session(engine) as session:
        statement = select(Game).where(Game.id == id_item)
        result = session.exec(statement)
        game = result.one()
        if  product.name != None:
            game.name = product.name
            session.add(game)
            session.commit()
            session.refresh(game)
        if product.price != None:
            game.price = product.price
            session.add(game)
            session.commit()
            session.refresh(game)
        if product.launch != None:
            game.launch = product.launch
            session.add(game)
            session.commit()
            session.refresh(game)
        
    return 'Product has been updated'