from azure.storage.blob import BlobServiceClient
from django.conf import settings
import os


def upload_picture_to_azure(file):
    account_url: str = (
        f"https://{settings.AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
    )

    blob_service_client = BlobServiceClient(
        account_url=account_url, credential=settings.AZURE_STORAGE_ACCOUNT_KEY
    )
    container_client = blob_service_client.get_container_client(
        settings.AZURE_STORAGE_CONTAINER_NAME
    )

    # Upload the picture
    blob_name = os.path.basename(file.name)
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file, overwrite=True)

    return blob_client.url
