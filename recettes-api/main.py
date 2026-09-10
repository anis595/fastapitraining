from fastapi import FastAPI

app = FastAPI(title="API Recettes du Nord", description="API Recettes du Nord")


@app.get("/")
def racine():
    return {"message": "API Recettes du Nord"}
