from azure.mgmt.compute.models import DiskCreateOption

poller = compute_client.disks.begin_create_or_update(
    'my_resource_group',
    'my_disk_name',
    {
        'location': 'eastus',
        'creation_data': {
            'create_option': DiskCreateOption.IMPORT,
            'storage_account_id': '/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Storage/storageAccounts/<storage-account-name>',
            'source_uri': 'https://<storage-account-name>.blob.core.windows.net/vm-images/test.vhd'
        }
    }
)
disk_resource = poller.result()