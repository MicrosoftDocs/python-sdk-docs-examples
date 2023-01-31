import os
import uuid
import asyncio

from azure.identity.aio import DefaultAzureCredential

# Import the client object from the SDK library
from azure.storage.blob.aio import BlobClient

# Retrieve the storage blob service URL, which is of the form
# https://<your-storage-account-name>.blob.core.windows.net/
storage_url = os.environ["AZURE_STORAGE_BLOB_URL"]

credential = DefaultAzureCredential()

async def run():

    async with BlobClient(
        storage_url,
        container_name="blob-container-01",
        blob_name=f"sample-blob-{str(uuid.uuid4())[0:5]}.txt",
        credential=credential,
    ) as blob_client:

        # Open a local file and upload its contents to Blob Storage
        with open("./sample-source.txt", "rb") as data:
            await blob_client.upload_blob(data)
            print(f"Uploaded sample-source.txt to {blob_client.url}")

        # Close credential
        await credential.close()

asyncio.run(run())
