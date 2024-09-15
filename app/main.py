from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world"}


@app.get("/{name}")
def root(name: str):
    return {"message": f"Hello {name}"}
