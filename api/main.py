from fastapi import FastAPI, Header

from src.models.schemas import AuditoriaXMLPayload


app = FastAPI(
    title="XML Auditoria API",
    description="API para receber payloads de auditoria XML processados pela automação Python.",
    version="1.0.0",
)


@app.get("/")
def healthcheck() -> dict[str, str]:
    return {
        "status": "online",
        "service": "xml-auditoria-api",
    }


@app.post("/api/auditoria/xml")
def receive_xml_audit(
    payload: AuditoriaXMLPayload,
    authorization: str | None = Header(default=None),
) -> dict[str, str | None]:
    # Production note:
    # This is the point where the payload should be persisted in a real database.
    # Recommended approach:
    # - Save important fields in indexed columns.
    # - Store the complete payload in a JSON/JSONB column.
    # - Use chave_acesso as a unique key to prevent duplicate processing.

    return {
        "status": "success",
        "message": "XML audit payload received successfully.",
        "arquivo": payload.arquivo,
        "chave_acesso": payload.dados.get("chave_acesso"),
    }
