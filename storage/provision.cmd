rem Provision the resource group

az group create ^
-n PythonAzureExample-Storage-rg ^
-l centralus

rem Provision the storage account

set account=pythonazurestorage%random%
echo Storage account name is %account%

az storage account create ^
-g PythonAzureExample-Storage-rg ^
-l centralus ^
-n %account% ^
--kind StorageV2 ^
--sku Standard_LRS

rem Retrieve the connection string

FOR /F %i IN ('az storage account show-connection-string -g PythonAzureExample-Storage-rg -n %account% --query connectionString') do (SET connstr=%i)

rem Provision the blob container

az storage container create ^
--name blob-container-01 ^
--account-name %account% ^
--connection-string %connstr%
