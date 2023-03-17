from azure.mgmt.compute.models import OperatingSystemStateTypes, HyperVGeneration

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