from service.cart.cart import Cart
from models.cart import CartModel
from typing import Union
from fastapi import FastAPI

app = FastAPI()

c1=Cart()


@app.get("/grocery")
def check_item_grocery():
    return c1.check_item_grocery()


@app.get("/beauty")
def check_item_beauty():
    return c1.check_item_beauty()


@app.get("/product_detail")
def product_detail(Item_name:str):
    return c1.product_detail(Item_name.capitalize())


@app.get("/check_stock")
def check_stock(Item_name:str):
    return c1.check_stock(Item_name.capitalize())

@app.get("/check_price")
def check_price(Item_name:str,quantity:int):
    return c1.check_price(Item_name.capitalize(),quantity)


@app.post("/buy_grocery")
def buy_grocery(Item_name:str,quantity:int):
    return c1.buy_grocery(Item_name.capitalize(),quantity)

@app.post("/add_product")
def add_product(cart:CartModel):
    Item_name=cart.Item_name
    Item_no=cart.Item_no
    Item_stock=cart.Item_stock
    Item_price=cart.Item_price
    return c1.add_item(Item_name.capitalize(),Item_no,Item_stock,Item_price)




