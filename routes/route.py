from fastapi import APIRouter
from sqlalchemy.sql.sqltypes import String
from config.db import conn, engine
from starlette.responses import JSONResponse

# from config.db import session
from model.articles import article
from model.fru_veg_model import fruveg
from model.fruit_model import fruits
from model.vegetable_model import vegetables
from schemas.fru_veg import FruVeg
from schemas.fruit import Fruit
from schemas.vegetable import Vegetable

# from fastapi import FastAPI, File, UploadFile

route = APIRouter()


@route.get('/nutria/get-all')
def fetch_all():
    # session.close()
    # return JSONResponse(content=fruveg.select()).fetchall()
    # try:
    with engine.begin() as connection:
        r1 = connection.execute(fruveg.select())
        # return connection.execute(fruveg.select()).fetchall()
        # return {'data': connection.execute(fruveg.select()).fetchall()}
        return {'data': conn.execute(fruveg.select()).fetchall()}
    # return {'data': conn.execute(fruveg.select()).fetchall()}
    # except:
    #     conn.rollback()
    #     conn.close()

# @route.get('/nutria/get_articles')
# def fetch_all_article():
#
#     return {'data': conn.execute(article.select()).fetchall()}


# @route.get('/nutria/get-fruit')
# def fetch_fruit():
#     return {'data': conn.execute(fruveg.select().where(fruveg.c.category == 'Fruit')).fetchall()}
#
#
# @route.get('/nutria/get-vegetable')
# def fetch_vegetable():
#     return {'data': conn.execute(fruveg.select().where(fruveg.c.category == 'Vegetable')).fetchall()}


# @route.post('/nutria/create-fruit/')
# def post_fruit(fruit: Fruit):
#     return conn.execute(fruits.insert().values(name=fruit.name, category=fruit.category, description=fruit.description))


# @route.post('/nutria/create-vegetable/')
# def post_vegetable(vegetable: Vegetable):
#     return conn.execute(
#         vegetables.insert().values(name=vegetable.name, category=vegetable.category, description=vegetable.description))


# @route.put('/nutria/update-fruit/{id}')
# def update_fruit(id: int, fruit: Fruit):
#     return conn.execute(
#         fruits.update().values(name=fruit.name, category=fruit.category, description=fruit.description).where(
#             fruits.c.id == id))


# @route.put('/nutria/update-vegetable/{id}')
# def update_vegetable(id: int, vegetable: Vegetable):
#     return conn.execute(
#         vegetables.update().values(name=vegetable.name, category=vegetable.category,
#                                    description=vegetable.description).where(vegetables.c.id == id))


# @route.get('/nutria/get-all/{name}')
# def fetch_one(name: str):
#     return conn.execute(fruveg.select().where(fruveg.c.name == name)).fetchall()


# @route.delete('/nutria/delete-fruit/{id}')
# def delete_fruit(id: int):
#     # c = column
#     return conn.execute(fruits.delete().where(fruits.c.id == id))
#
#
# @route.delete('/nutria/delete-vegetable/{id}')
# def delete_vegetable(id: int):
#     # c = column
#     return conn.execute(vegetables.delete().where(vegetables.c.id == id))
