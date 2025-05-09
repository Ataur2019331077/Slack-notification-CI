from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}


@app.get("/check")
def check():
    return {"message": "Check endpoint is working"}

@app.get("/new-endpoint")
def new_endpoint():
    return {"message": "This is a new endpoint!"}

@app.get("/adding-subbranch")
def adding_subbranch():
    return {"message": "This is a new subbranch!"}

