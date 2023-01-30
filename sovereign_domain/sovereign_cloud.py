import os
from msrestazure.azure_cloud import AZURE_CHINA_CLOUD as CLOUD
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.identity import DefaultAzureCredential, AzureAuthorityHosts

# Set environment variable AZURE_SUBSCRIPTION_ID as well as environment variables
# for DefaultAzureCredential. For combinations of environment variables, see
# https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#environment-variables
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

# When using sovereign domains (that is, any cloud other than AZURE_PUBLIC_CLOUD),
# you must use an authority with DefaultAzureCredential.
credential = DefaultAzureCredential(authority=AzureAuthorityHosts.AZURE_CHINA)

resource_client = ResourceManagementClient(
    credential, subscription_id,
    base_url=CLOUD.endpoints.resource_manager,
    credential_scopes=[CLOUD.endpoints.resource_manager + "/.default"])

subscription_client = SubscriptionClient(
    credential,
    base_url=CLOUD.endpoints.resource_manager,
    credential_scopes=[CLOUD.endpoints.resource_manager + "/.default"])
