import os

from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import OperatingSystemStateTypes, HyperVGeneration

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

compute_client = ComputeManagementClient(credential, subscription_id)

poller = compute_client.images.begin_create_or_update(
    'my_resource_group',
    'my_disk_name',
    {
        'location': 'eastus',
        'storage_profile': {
           'os_disk': {
              'os_type': 'Linux',
              'os_state': OperatingSystemStateTypes.GENERALIZED,
              'blob_uri': 'https://<storage-account-name>.blob.core.windows.net/vm-images/test.vhd',
              'caching': "ReadWrite",
           },
        },
        'hyper_v_generation': HyperVGeneration.V2,
    }
)
image_resource = poller.result()