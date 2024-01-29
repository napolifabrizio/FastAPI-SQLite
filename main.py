from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session, select
from models.Game import Game

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