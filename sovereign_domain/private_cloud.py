import os
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.identity import DefaultAzureCredential
from azure.profiles import KnownProfiles

# Set environment variable AZURE_SUBSCRIPTION_ID as well as environment variables
# for DefaultAzureCredential. For combinations of environment variables, see
# https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#environment-variables
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

authority = "<your authority>"
endpoint = "<your endpoint>"
audience = "<your audience>"

# When using a private cloud, you must use an authority with DefaultAzureCredential.
# The active_directory endpoint should be a URL like https://login.microsoftonline.com.
credential = DefaultAzureCredential(authority=authority)

resource_client = ResourceManagementClient(
    credential, subscription_id,
    base_url=endpoint,
    profile=KnownProfiles.v2019_03_01_hybrid,
    credential_scopes=[audience])

subscription_client = SubscriptionClient(
    credential,
    base_url=endpoint,
    profile=KnownProfiles.v2019_03_01_hybrid,
    credential_scopes=[audience])
 