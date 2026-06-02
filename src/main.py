from datetime import datetime
from pathlib import Path
from typing import Any

from src.config import (
    API_ENDPOINT,
    API_TOKEN,
    GOOGLE_CREDENTIALS_FILE,
    GOOGLE_DRIVE_FOLDER_ID,
    OUTPUT_DIR,
    TEMP_DIR,
    validate_config,
)
from src.services.api_client import APIClient
from src.services.google_drive_service import GoogleDriveService
from src.services.xml_processor import XMLAuditProcessor
from src.utils.logger import setup_logger


logger = setup_logger()


def build_audit_payload(file_name: str, xml_data: dict[str, Any]) -> dict[str, Any]:
    return {
        "arquivo": file_name,
        "origem": "GOOGLE_DRIVE",
        "tipo_documento": "XML_NFE",
        "status": "PROCESSADO",
        "processado_em": datetime.now().isoformat(),
        "dados": xml_data,
    }


def process_file(file_metadata: dict[str, Any], drive_service: GoogleDriveService, api_client: APIClient) -> None:
    file_name = file_metadata["name"]

    logger.info("Processing XML file: %s", file_name)

    local_xml_path = drive_service.download_file(
        file_id=file_metadata["id"],
        file_name=file_name,
        destination=TEMP_DIR,
    )

    processor = XMLAuditProcessor(local_xml_path)
    extracted_data = processor.extract_with_xpath()
    payload = build_audit_payload(file_name, extracted_data)

    base_name = Path(file_name).stem
    json_output_path = str(Path(OUTPUT_DIR) / f"{base_name}.json")
    xml_output_path = str(Path(OUTPUT_DIR) / f"{base_name}_auditado.xml")

    processor.save_json(payload, json_output_path)
    processor.append_audit_marker(xml_output_path)

    api_response = api_client.send_audit_payload(payload)

    logger.info("Payload sent successfully: %s", api_response)


def main() -> None:
    validate_config()

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    Path(TEMP_DIR).mkdir(parents=True, exist_ok=True)

    drive_service = GoogleDriveService(GOOGLE_CREDENTIALS_FILE)
    api_client = APIClient(API_ENDPOINT, API_TOKEN)

    xml_files = drive_service.list_xml_files(GOOGLE_DRIVE_FOLDER_ID)

    if not xml_files:
        logger.info("No XML files found in Google Drive folder.")
        return

    for file_metadata in xml_files:
        try:
            process_file(file_metadata, drive_service, api_client)
        except Exception as error:
            logger.exception(
                "Failed to process file %s: %s",
                file_metadata.get("name"),
                error,
            )


if __name__ == "__main__":
    main()
