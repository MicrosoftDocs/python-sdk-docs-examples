az group create --location southcentralus --name PythonAzureExample-DB-rg

az mysql flexible-server create --location southcentralus --resource-group PythonAzureExample-DB-rg \
    --name python-azure-example-mysql-12345 --admin-user azureuser --admin-password ChangePa$$w0rd24 \
    --sku-name Standard_B1ms --version 5.7 --yes

# Change the IP address to the public IP address of your workstation, that is, the address shown
# by a site like https://whatismyipaddress.com/.

az mysql flexible-server firewall-rule create --resource-group PythonAzureExample-DB-rg --name python-azure-example-mysql-12345 \
    --rule-name allow_ip --start-ip-address 10.11.12.13 --end-ip-address 10.11.12.13

az mysql flexible-server db create --resource-group PythonAzureExample-DB-rg --server-name python-azure-example-mysql-12345 \
    --database-name example-db1
