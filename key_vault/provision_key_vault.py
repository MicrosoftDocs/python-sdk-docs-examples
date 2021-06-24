import os, random
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.keyvault.models import VaultCreateOrUpdateParameters
from azure.mgmt.keyvault.models import VaultProperties
from azure.mgmt.keyvault.models import Sku
from azure.mgmt.keyvault.models import Permissions
from azure.mgmt.keyvault.models import AccessPolicyEntry

tenant_id = os.environ["AZURE_TENANT_ID"]
object_id = os.environ["AZURE_CLIENT_ID"]

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]


# Step 1: Provision a resource group

# Obtain the management object for resources, using the credentials from the CLI login.
resource_client = ResourceManagementClient(credential, subscription_id)

# Constants we need in multiple places: the resource group name and the region
# in which we provision resources. You can change these values however you want.
RESOURCE_GROUP_NAME = "PythonAzureExample-KeyVault-rg"
LOCATION = "westus2"

# Provision the resource group.
rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
    {
        "location": LOCATION
    }
)


print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")

# For details on the previous code, see Example: Provision a resource group
# at https://docs.microsoft.com/azure/developer/python/azure-sdk-example-resource-group


# Step 2: Provision key vaults using two equivalent methods.

# 
keyvault_client = KeyVaultManagementClient(credential, subscription_id)

KEY_VAULT_BASE_NAME = os.getenv("KEY_VAULT_BASE_NAME", f"python-keyvault-{random.randint(1,100000):05}")

KEY_VAULT_NAME_A = KEY_VAULT_BASE_NAME + "aa"
KEY_VAULT_NAME_B = KEY_VAULT_BASE_NAME + "bb"

# Check if the names are available; they must be unique across Azure because they're used in URLs.
for name in [KEY_VAULT_NAME_A, KEY_VAULT_NAME_B]:
    availability_result = keyvault_client.vaults.check_name_availability(
        { "name": name }
    )

    if not availability_result.name_available:
        print(f"Key Vault name {name} is not available. Try another name.")
        exit()


# Provision a Key Vault using inline parameters
poller = keyvault_client.vaults.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    KEY_VAULT_NAME_A,
    VaultCreateOrUpdateParameters(
        location = "centralus",
        properties = VaultProperties(
            tenant_id = tenant_id,
            sku = Sku(
                name="standard",
                family="A"
            ),            
            access_policies = [
                AccessPolicyEntry(
                    tenant_id = tenant_id,
                    object_id = object_id,
                    permissions = Permissions(
                        keys = ['all'],
                        secrets = ['all']
                    )
                )
            ]
        )
    )
)

key_vault1 = poller.result()

print(f"Provisioned key vault {key_vault1.name} in the {key_vault1.location} region")


# Provision a Key Vault using inline JSON

poller = keyvault_client.vaults.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    KEY_VAULT_NAME_B,
    {
        'location': 'centralus',
        'properties': {
            'sku': {
                'name': 'standard',
                'family': 'A'
            },
            'tenant_id': tenant_id,
            'access_policies': [{
                'tenant_id': tenant_id,
                'object_id': object_id,                
                'permissions': {
                    'keys': ['all'],
                    'secrets': ['all']
                }
            }]
        }
    }
)

key_vault2 = poller.result()

print(f"Provisioned key vault {key_vault2.name} in the {key_vault2.location} region")
