# from fastapi import FastAPI
# from api.routes import router

# app = FastAPI(title="İnsanekspertizi API")

# app.include_router(router)

# @app.get("/")
# def root():
#     return {"status": "İnsanekspertizi çalışıyor"}

from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="İnsan Ekspertizi API")

app.include_router(router)