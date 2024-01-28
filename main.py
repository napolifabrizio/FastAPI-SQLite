from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def start():
    print('Welcome to my API')