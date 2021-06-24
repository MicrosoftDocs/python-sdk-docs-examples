import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# To enable deeper logging, use logging.getLogger with the name of the 
# SDK module you care about. When set the logging level and add a handler
# for stdout. 
import sys, logging

# azure.core.pipeline.policies generates log output for all REST API
# request/response transactions. 
# azure.core.pipeline.policies
logger = logging.getLogger('azure')
logger.setLevel(logging.INFO)

# Add a handler to the logger for stdout; you can use a different stream
# for different output, if desired.
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

keyVaultName = os.environ["KEY_VAULT_NAME"]
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential, logging_enable=True)

# secret_name' must conform to the following pattern: ^[0-9a-zA-Z-]
secretName = "secret-name-09"
secretValue = input("Enter a value for your secret: ")

print(f"Creating secret {secretName} in vault {keyVaultName} with the value {secretValue}...")

client.set_secret(secretName, secretValue)

input("Press any key to retrieve the secret from the KeyVault.")

retrieved_secret = client.get_secret(secretName)

print(f"Your secret's value from the KeyVault is {retrieved_secret.value}")

input(f"Press any key to delete your secret and attempt to retrieve again.")

client.begin_delete_secret(secretName)

try:
    retrieved_secret = client.get_secret(secretName)
    print(f"Your deleted secret's value from the KeyVault is {retrieved_secret.value}")
except:
    print("Your secret was no longer found in the KeyVault.")
