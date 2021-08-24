# Python Azure Dev Center SDK Samples

This repository contains code used in articles on the [Azure for Python Developers](https://docs.microsoft.com/en-us/azure/developer/python/) site.

Much of the code appears in the SDK examples starting with [Provision a resource group](https://docs.microsoft.com/azure/developer/python/azure-sdk-example-resource-group).

See the individual source files for the articles that use the code.

Other folders contain Python snippets used in the documentation. Some of the files are snippets only, rather than full samples, and are not runnable. Contributions to make these snippets runnable are welcome.

Note also that the [docs source files](https://github.com/MicrosoftDocs/azure-dev-docs) contain direct line number references to some of the files in this repo, so changes to these files may require changes to the docs.

## Running the samples

1. Follow the instructions on [Set up your dev environment](https://docs.microsoft.com/azure/developer/python/configure-local-development-environment?tabs=cmd). The samples depend on the environment variables described in that article: AZURE_SUBSCRIPTION_ID, AZURE_TENANT_ID, AZURE_CLIENT_ID, and AZURE_CLIENT_SECRET. 

1. In the sample folder of your choice, create and activate a virtual environment and install dependencies:

    ```
    python -m venv .venv
    .venv\scripts\activate  # Linux: source bin/scripts/activate
    pip install -r requirements.txt
    ```

1. Check the code for any additional environment variables you may need to define. The article associated with the code explains these details.

1. Run `python` with the script of your choice.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
