from fastapi import FastAPI, Depends, HTTPException
from routers import roles, memberships, users, petstype, pets, matchs, auth
from database import models, schemes
from database.database import engine
from utils.auth import role_required

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(
    router=roles.router,
    tags=["Crud Roles"]
)
app.include_router(
    router=memberships.router,
    tags=["Crud Memberships"]
)
app.include_router(
    router=users.router,
    tags=["Crud Users"]
)
app.include_router(
    router=petstype.router,
    tags=["Crud Pets Type"]
)
app.include_router(
    router=pets.router,
    tags=["Crud Pets"]
)
app.include_router(
    router=matchs.router,
    tags=["Crud Matchs"]
)
app.include_router(
    router=auth.router,
    tags=["Auth Endpoints"]
)