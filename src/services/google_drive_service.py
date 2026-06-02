import io
from pathlib import Path
from typing import Any

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


class GoogleDriveService:
    """Service responsible for listing and downloading XML files from Google Drive."""

    def __init__(self, credentials_file: str):
        credentials = service_account.Credentials.from_service_account_file(
            credentials_file,
            scopes=SCOPES,
        )

        self.service = build("drive", "v3", credentials=credentials)

    def list_xml_files(self, folder_id: str) -> list[dict[str, Any]]:
        query = (
            f"'{folder_id}' in parents "
            "and mimeType != 'application/vnd.google-apps.folder' "
            "and trashed = false"
        )

        response = self.service.files().list(
            q=query,
            fields="files(id, name, mimeType, modifiedTime)",
        ).execute()

        files = response.get("files", [])

        return [file for file in files if file["name"].lower().endswith(".xml")]

    def download_file(self, file_id: str, file_name: str, destination: str) -> str:
        Path(destination).mkdir(parents=True, exist_ok=True)

        local_path = Path(destination) / file_name
        request = self.service.files().get_media(fileId=file_id)

        with io.FileIO(local_path, "wb") as file_handler:
            downloader = MediaIoBaseDownload(file_handler, request)
            done = False

            while not done:
                _, done = downloader.next_chunk()

        return str(local_path)
