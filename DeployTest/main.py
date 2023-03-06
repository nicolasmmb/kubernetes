from typing import Final
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import os

ROOT_PATH: Final[str] = os.environ.get("ROOT_PATH", "/")
VERSION: Final[str] = os.environ.get("VERSION", "X")

app = FastAPI(
    root_path=ROOT_PATH,
    version=VERSION,
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/all", tags=["ENVs"])
async def read_all_envs():
    values = {k: v for k, v in os.environ.items()}
    return {k: values[k] for k in sorted(values)}


@app.get("/health-check", tags=["TEST"], status_code=200)
async def read_health_check():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
async def redirect_docs():
    return RedirectResponse("/docs")
