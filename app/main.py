from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
import os
import jwt
from jwt import PyJWTError
from datetime import datetime
from .schemas import DevOpsPayload
from .config import API_KEY, JWT_SECRET, JWT_ALGORITHM

app = FastAPI(title="DevOps Challenge Service")

@app.middleware("http")
async def only_devops_route(request: Request, call_next):

    if request.url.path != "/DevOps":
        return await call_next(request)

    if request.method != "POST":
        return PlainTextResponse("ERROR", status_code=405)
    return await call_next(request)

@app.post("/DevOps")
async def devops_endpoint(
    payload: DevOpsPayload,
    x_parse_rest_api_key: str = Header(None, alias="X-Parse-REST-API-Key"),
    x_jwt_kwy: str = Header(None, alias="X-JWT-KWY")
):

    if x_parse_rest_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API Key Invalida")

    if not x_jwt_kwy:
        raise HTTPException(status_code=401, detail="JWT Faltante")

    try:
        decoded = jwt.decode(x_jwt_kwy, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except PyJWTError:
        raise HTTPException(status_code=401, detail="JWT Invalido")

    if "jti" not in decoded:
        raise HTTPException(status_code=400, detail="JWT  tiene que incluir el campo jti")

    iat = decoded.get("iat")
    if not iat:
        raise HTTPException(status_code=400, detail="JWT iene que incluir el campo iat")
    now_ts = int(datetime.utcnow().timestamp())
    if abs(now_ts - int(iat)) > 300:
        raise HTTPException(status_code=401, detail="JEl iat del JWT está fuera del rango permitido")

    resp = {"message": f"Hello {payload.to} your message will be sent"}
    return JSONResponse(content=resp)
