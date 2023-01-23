# Provision the resource group

az group create \
-n PythonAzureExample-Storage-rg \
-l centralus

# Provision the storage account

ACCOUNT_NAME=pythonazurestorage$(echo $RANDOM | md5sum | head -c 6)

az storage account create \
-g PythonAzureExample-Storage-rg \
-l centralus \
-n $ACCOUNT_NAME \
--kind StorageV2 \
--sku Standard_LRS

# Retrieve the connection string

echo Storage account name is $ACCOUNT_NAME

CONNECTION_STRING=$(az storage account show-connection-string \
-g PythonAzureExample-Storage-rg \
-n $ACCOUNT_NAME \
--query connectionString)

# Provision the blob container

az storage container create --name "blob-container-01" \
--account-name $ACCOUNT_NAME \
--connection-string $CONNECTION_STRING
