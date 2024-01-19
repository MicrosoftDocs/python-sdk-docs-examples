import logging
import os
import sys
import uuid

from azure.core import exceptions
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

logger = logging.getLogger("azure")
logger.setLevel(logging.DEBUG)

# Set the logging level for the azure.storage.blob library
logger = logging.getLogger("azure.storage.blob")
logger.setLevel(logging.DEBUG)

print(
    f"Logger enabled for ERROR={logger.isEnabledFor(logging.ERROR)}, "
    f"WARNING={logger.isEnabledFor(logging.WARNING)}, "
    f"INFO={logger.isEnabledFor(logging.INFO)}, "
    f"DEBUG={logger.isEnabledFor(logging.DEBUG)}"
)

# Direct logging output to stdout. Without adding a handler,
# no logging output is visible.
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

try:
    credential = DefaultAzureCredential()
    storage_url = os.environ["AZURE_STORAGE_BLOB_URL"]
    unique_str = str(uuid.uuid4())[0:5]

    # Enable logging on the client object
    blob_client = BlobClient(
        storage_url,
        container_name="blob-container-01",
        blob_name=f"sample-blob-{unique_str}.txt",
        credential=credential,
    )

    with open("./sample-source.txt", "rb") as data:
        blob_client.upload_blob(data, logging_body=True, logging_enable=True)

except (
    exceptions.ClientAuthenticationError,
    exceptions.HttpResponseError
) as e:
    print(e.message)
