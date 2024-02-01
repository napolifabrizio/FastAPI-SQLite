from fastapi import FastAPI, HTTPException
from source.config.produto_repo import ProdutoConfig
from source.models.Game import Game

app = FastAPI()

@app.get('/')
def start():
    return 'Welcome to my API'

@app.get('/show_products')
def get_products():
    products = ProdutoConfig.get_products(Game)
    return products

@app.get('/show_product/{id_item}')
def get_product(id_item: int):
    product = ProdutoConfig.get_product(id_item, Game)
    return product

@app.post('/insert_product')
def post_product(product: Game):
    ProdutoConfig.post_product(product)
    return 'The product has been inserted'

# @app.put('/update_product/{id_item}')
# def put_product(id_item: int, product: Game):
#     with Session(engine) as session:
#         try:
#             statement = select(Game).where(Game.id == id_item)
#             result = session.exec(statement)
#             game = result.one()
#         except:
#             raise HTTPException(404, 'Product not found')
        
#         if  product.name != None:
#             game.name = product.name
#         if product.price != None:
#             game.price = product.price
#         if product.launch != None:
#             game.launch = product.launch
#         session.add(game)
#         session.commit()
#         session.refresh(game)
        
#     return 'The product has been updated'

# @app.delete('/delete_product/{id_item}')
# def delete_product(id_item: int):
#     with Session(engine) as session:
#         try:
#             statement = select(Game).where(Game.id == id_item)
#             result = session.exec(statement)
#             game = result.one()
#         except:
#             raise HTTPException(404, 'Product not found')
#         session.delete(game)
#         session.commit()

#     return 'The product has been deleted'

        