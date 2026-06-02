from typing import Any

from pydantic import BaseModel


class AuditoriaXMLPayload(BaseModel):
    arquivo: str
    origem: str
    tipo_documento: str
    status: str
    processado_em: str
    dados: dict[str, Any]
