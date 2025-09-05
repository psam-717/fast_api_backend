from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id=1, name="Samsung", description='A smart phone', price=10.56, quantity=30),
    Product(id=2, name="Macbook", description='A laptop', price=10.56, quantity=30),
    Product(id=3, name="Bic", description='Pen', price=10.56, quantity=30),
    Product(id=4, name="Note book", description='Stationery', price=10.56, quantity=30),
    Product(id=5, name="Nasco", description='Fridge', price=10.56, quantity=30)
]

@app.get('/')
def welcome_message(): 
    return {'Hello': 'Welcome'}

@app.get('/products')
def get_all_products():
    return (products)

#retrieving product by id
@app.get('/product{id}')
def get_product_by_id(id: int):
    return(products[id - 1])


@app.get('/home')
async def home_message():
    return{'Welcome home'}