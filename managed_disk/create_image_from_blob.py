async_create_image = compute_client.images.create_or_update(
    'my_resource_group',
    'myImage',
    {
        'location': 'eastus',
        'storage_profile': {
            'os_disk': {
                'os_type': 'Linux',
                'os_state': "Generalized",
                'blob_uri': 'https://<storage-account-name>.blob.core.windows.net/vm-images/test.vhd',
                'caching': "ReadWrite",
            }
        }
    }
)
image = async_create_image.result()