from fastapi import FastAPI
from routes import auth_routes, pen_routes

app = FastAPI()

app.include_router(auth_routes)
app.include_router(pen_routes)

@app.get('/')
def root():
    return {'message' : 'sex'}
