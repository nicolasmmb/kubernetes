from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/timer", tags=["Timer"])
async def read_timer(interval: int = 5):
    import time

    time.sleep(interval)
    return {"interval": interval}


@app.get("/error", tags=["Error"])
async def read_error():
    raise ValueError("This is an error")


@app.get("/all_env_vars", tags=["ENVs"])
async def read_all_env_vars():
    import os

    values = {k: v for k, v in os.environ.items()}
    return {k: values[k] for k in sorted(values)}


@app.get("/health-check", tags=["TEST"], status_code=200)
async def read_health_check():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
async def redirect_docs():
    return RedirectResponse("/docs")
