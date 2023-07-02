from pydantic import BaseModel

class CartModel(BaseModel):
    Item_name:str
    Item_no:int
    Item_stock:int
    Item_price:int