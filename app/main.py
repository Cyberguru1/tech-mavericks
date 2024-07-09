#!/usr/bin/python3

from routers import user, insurance, hospital, patient, auth
from config.config import settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
import sys
sys.path.insert(0, '..')


# sys.path.insert(0, '..')

app = FastAPI()

#  add session middleware for google login
app.add_middleware(SessionMiddleware, secret_key=settings.secret_key)

origins = ["http://localhost:8080", "https://tech-maverics.onrender.com", "https://tech-marverick.netlify.app"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(insurance.router)
app.include_router(hospital.router)
app.include_router(patient.router)
