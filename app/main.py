"""Etapa 4 — a API e a página.

Rodar localmente:  uv run uvicorn app.main:app --reload   →  http://127.0.0.1:8000
"""

from decimal import Decimal
from pathlib import Path

import segno
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from pix.payload import build_static_payload  # noqa: F401  (você vai usar)

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Pix por dentro", version="0.1.0")


class PixEntrada(BaseModel):
    chave: str = Field(min_length=1, max_length=77)
    nome: str = Field(min_length=1, max_length=60)
    cidade: str = Field(min_length=1, max_length=60)
    valor: Decimal | None = Field(default=None, gt=0, decimal_places=2)
    txid: str = "***"
    info_adicional: str | None = Field(default=None, max_length=72)


class PixSaida(BaseModel):
    payload: str
    qr_svg: str


def gerar_svg(payload: str) -> str:
    # make_qr força QR comum (sem micro QR); "m" = correção de erro média (~15%).
    return segno.make_qr(payload, error="m").svg_inline(scale=6, border=2)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
def pagina() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/api/pix", response_model=PixSaida)
def gerar_pix(entrada: PixEntrada) -> PixSaida:
    # TODO (Etapa 4):
    # 1. chame build_static_payload com os campos de `entrada`
    # 2. se ela levantar ValueError, transforme em HTTPException(status_code=422, detail=str(erro))
    #    use `raise ... from erro` para não perder a causa
    # 3. devolva PixSaida(payload=..., qr_svg=gerar_svg(...))
    raise HTTPException(status_code=501, detail="Etapa 4: ligue a API ao gerador")


class DecodificarEntrada(BaseModel):
    payload: str = Field(min_length=8, max_length=512)


@app.post("/api/decodificar")
def decodificar_pix(entrada: DecodificarEntrada) -> dict:
    # TODO (bônus): chame pix.decoder.decodificar e trate ValueError como no endpoint acima.
    # Lembre: Decimal vira string no JSON (FastAPI faz isso por você).
    raise HTTPException(status_code=501, detail="Bônus: decodificador ainda não implementado")
