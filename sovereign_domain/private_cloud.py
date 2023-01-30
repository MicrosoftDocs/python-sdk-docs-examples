import os
from msrestazure.azure_cloud import get_cloud_from_metadata_endpoint
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.identity import DefaultAzureCredential
from azure.profiles import KnownProfiles

# Set environment variable AZURE_SUBSCRIPTION_ID as well as environment variables
# for DefaultAzureCredential. For combinations of environment variables, see
# https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#environment-variables
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

stack_cloud = get_cloud_from_metadata_endpoint("https://contoso-azurestack-arm-endpoint.com")

# When using a private cloud, you must use an authority with DefaultAzureCredential.
# The active_directory endpoint should be a URL like https://login.microsoftonline.com.
credential = DefaultAzureCredential(authority=stack_cloud.endpoints.active_directory)

resource_client = ResourceManagementClient(
    credential, subscription_id,
    base_url=stack_cloud.endpoints.resource_manager,
    profile=KnownProfiles.v2019_03_01_hybrid,
    credential_scopes=[stack_cloud.endpoints.active_directory_resource_id + "/.default"])

subscription_client = SubscriptionClient(
    credential,
    base_url=stack_cloud.endpoints.resource_manager,
    profile=KnownProfiles.v2019_03_01_hybrid,
    credential_scopes=[stack_cloud.endpoints.active_directory_resource_id + "/.default"])
