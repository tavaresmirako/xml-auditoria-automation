import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_DRIVE_FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID", "")
GOOGLE_CREDENTIALS_FILE = os.getenv(
    "GOOGLE_CREDENTIALS_FILE",
    "credentials/service_account.json",
)

API_ENDPOINT = os.getenv("API_ENDPOINT", "http://localhost:8000/api/auditoria/xml")
API_TOKEN = os.getenv("API_TOKEN", "")

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")
TEMP_DIR = os.getenv("TEMP_DIR", "temp")


def validate_config() -> None:
    required = {
        "GOOGLE_DRIVE_FOLDER_ID": GOOGLE_DRIVE_FOLDER_ID,
        "GOOGLE_CREDENTIALS_FILE": GOOGLE_CREDENTIALS_FILE,
        "API_ENDPOINT": API_ENDPOINT,
    }

    missing = [key for key, value in required.items() if not value]

    if missing:
        raise ValueError(
            "Configuração incompleta. Variáveis ausentes: " + ", ".join(missing)
        )
