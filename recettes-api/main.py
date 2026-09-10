from fastapi import FastAPI, HTTPException

app = FastAPI(title="API Recettes du Nord", description="API Recettes du Nord")


@app.get("/")
def racine():
    return {"message": "API Recettes du Nord"}


@app.get("/health")
def health():
    return {"status": "ok"}


RECETTES = [
    {
        "id_recette": 1,
        "nom": "Carbonnade flamande",
        "difficulte": 2,
        "temps_minutes": 180,
        "vegetarien": False,
    },
    {
        "id_recette": 2,
        "nom": "Welsh complet",
        "difficulte": 1,
        "temps_minutes": 30,
        "vegetarien": False,
    },
    {
        "id_recette": 3,
        "nom": "Tarte au maroilles",
        "difficulte": 2,
        "temps_minutes": 60,
        "vegetarien": True,
    },
    {
        "id_recette": 4,
        "nom": "Potjevleesch",
        "difficulte": 3,
        "temps_minutes": 240,
        "vegetarien": False,
    },
    {
        "id_recette": 5,
        "nom": "Soupe de chicons",
        "difficulte": 1,
        "temps_minutes": 45,
        "vegetarien": True,
    },
]

recettes = []


@app.get("/recettes")
def get_recettes():
    return RECETTES
