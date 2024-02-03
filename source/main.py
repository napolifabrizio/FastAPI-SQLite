from fastapi import FastAPI
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

@app.put('/update_product/{id_item}')
def put_product(id_item: int, product: Game):
    ProdutoConfig.put_product(id_item, product, Game) 
    return 'The product has been updated'

@app.delete('/delete_product/{id_item}')
def delete_product(id_item: int):
    ProdutoConfig.delete_product(id_item, Game)
    return 'The product has been deleted'

        