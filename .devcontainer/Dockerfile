FROM python:3.11

# Install the Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install the Azure Functions Core Tools: https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
RUN sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/debian/$(lsb_release -rs 2>/dev/null \ 
    | cut -d'.' -f 1)/prod $(lsb_release -cs 2>/dev/null) main" > /etc/apt/sources.list.d/dotnetdev.list'
RUN apt-get update
RUN apt-get install azure-functions-core-tools-4
