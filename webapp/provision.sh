# Replace <your_github_user_name> with the account name of the fork.

REPO_URL="https://github.com/<your_github_user_name>/python-docs-hello-world"
APP_NAME=PythonAzureExample-WebApp-$(echo $RANDOM | md5sum | head -c 6)

az group create -l centralus -n PythonAzureExample-WebApp-rg

az appservice plan create -n PythonAzureExample-WebApp-plan -g PythonAzureExample-WebApp-rg \
   --is-linux --sku F1

echo "Creating app : "$APP_NAME
az webapp create -g PythonAzureExample-WebApp-rg -n $APP_NAME \
    --plan PythonAzureExample-WebApp-plan --runtime "python|3.8"

# You can use --deployment-source-url with the first create command. It is shown here
# to match the sequence of the Python code.

az webapp create -n $APP_NAME -g PythonAzureExample-WebApp-rg \
    --plan PythonAzureExample-WebApp-plan --runtime "python|3.8" \
    --deployment-source-url $REPO_URL

# The previous command sets up External Git deployment from the specified repository. This 
# command triggers a pull from the repository.

az webapp deployment source sync --name $APP_NAME --resource-group PythonAzureExample-WebApp-rg
