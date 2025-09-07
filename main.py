from fastapi import FastAPI
import routes, models, database

# create the fastpi app
app = FastAPI(title='Items API', description='API for managing items')

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

# Include router from the routes.py file
app.include_router(routes.router, prefix='/api', tags=["items"])

@app.get('/welcome')
def welcome_message():
    return {"message": "Hello there"}