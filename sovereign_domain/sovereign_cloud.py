import os
from msrestazure.azure_cloud import AZURE_CHINA_CLOUD as CLOUD
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.identity import DefaultAzureCredential

# Assumes the subscription ID and tenant ID to use are in the AZURE_SUBSCRIPTION_ID and
# AZURE_TENANT_ID environment variables
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
tenant_id = os.environ["AZURE_TENANT_ID"]

# When using sovereign domains (that is, any cloud other than AZURE_PUBLIC_CLOUD),
# you must use an authority with DefaultAzureCredential.
credential = DefaultAzureCredential(authority=CLOUD.endpoints.active_directory, tenant_id=tenant_id)

resource_client = ResourceManagementClient(
    credential, subscription_id,
    base_url=CLOUD.endpoints.resource_manager,
    credential_scopes=[CLOUD.endpoints.resource_manager + "/.default"])

subscription_client = SubscriptionClient(
    credential,
    base_url=CLOUD.endpoints.resource_manager,
    credential_scopes=[CLOUD.endpoints.resource_manager + "/.default"])