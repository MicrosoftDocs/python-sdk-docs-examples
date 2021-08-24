from azure.storage.blob import BlobClient
from azure.identity import DefaultAzureCredential

# endpoint is the Blob storage URL.
client = BlobClient(endpoint, DefaultAzureCredential())

# Enable HTTP logging for only this operation when using DEBUG level
client.create_container("container01", logging_enable=True)
