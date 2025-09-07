# from fastapi import FastAPI, HTTPException
# from models import Product

# app = FastAPI()

# products = [
#     Product(id=1, name="Samsung", description='A smart phone', price=10.56, quantity=30),
#     Product(id=2, name="Macbook", description='A laptop', price=10.56, quantity=30),
#     Product(id=3, name="Bic", description='Pen', price=10.56, quantity=30),
#     Product(id=4, name="Note book", description='Stationery', price=10.56, quantity=30),
#     Product(id=5, name="Nasco", description='Fridge', price=10.56, quantity=30)
# ]

# @app.get('/')
# def welcome_message(): 
#     return {'Hello': 'Welcome'}

# @app.get('/home')
# async def home_message():
#     return{'Welcome home'}

# @app.get('/products')
# def get_all_products():
#     return (products)


# #retrieving product by id
# @app.get('/product/{product_id}')
# def get_product_by_id(product_id: int):
#     for product in products:
#         if(product.id == product_id):
#             return product
#     raise HTTPException(status_code=404, detail='Product not found')


# # add new product to inventory
# @app.post('/add-product')
# def add_product(product: Product):
#     try:
#         # if the product already exists
#         for single_product in products:
#             if(single_product.name == product.name):
#                 raise HTTPException(status_code=400, detail="Product already in inventory")
#         products.append(product)
#         return {"message": "Product added successfully", "product": product}
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=f"Invalid product data: {str(e)}") from e


# @app.put('/update-product')
# def update_product(product_id: int, product: Product): # product_id is a query parameter since it is not specified in the req body
#     #ensure that the product_id in the query matches the id specified in the req body
#     if product.id != product_id:
#         raise HTTPException(status_code=400, detail="Product Id does not match")
#     for idx, existing_product in enumerate(products):
#         # fetch product whose id matches the product_id specified in the quesry
#         if existing_product.id == product_id:
#             products[idx] = product
#             return {"message": "Product updated successfully", "product": product}
#     # if product does not exist
#     raise HTTPException(status_code=404, detail="product not found")


# @app.delete('/delete-product/{product_id}')
# def delete_product(product_id: int):
#     for idx, existing_product in enumerate(products):
#         if existing_product.id == product_id:
#             deleted_product = products.pop(idx)
#             return {"message": "Product deleted successfully", "deleted_product": deleted_product}
#     # if product with id does not exist
#     raise HTTPException(status_code=404, detail='product not found')