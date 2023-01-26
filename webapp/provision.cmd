rem Replace <your_github_user_name> with the account name of the fork.

set repoUrl=https://github.com/<your_github_user_name>/python-docs-hello-world
set appName=PythonAzureExample-WebApp-%random%

az group create -l centralus -n PythonAzureExample-WebApp-rg

az appservice plan create -n PythonAzureExample-WebApp-plan -g PythonAzureExample-WebApp-rg ^
     --is-linux --sku F1

echo Creating app: %appName%

az webapp create -g PythonAzureExample-WebApp-rg -n %appName% ^
    --plan PythonAzureExample-WebApp-plan --runtime "python|3.8"

rem You can use --deployment-source-url with the first create command. It is shown here
rem to match the sequence of the Python code.

az webapp create -n %appName% -g PythonAzureExample-WebApp-rg ^
    --plan PythonAzureExample-WebApp-plan --runtime "python|3.8" ^
    --deployment-source-url %repoUrl% 
