name: Deploy Java Function App to Azure

on:
  push:
    branches: [ main ]
  workflow_dispatch:

env:
  AZURE_FUNCTIONAPP_NAME: 'javafunctionappjp'
  FUNCTION_PROJECT_PATH: 'AzureJavaFunctionDeploy'  # Corrected variable name
  JAVA_VERSION: '11'

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Java
        uses: actions/setup-java@v3
        with:
          java-version: ${{ env.JAVA_VERSION }}
          distribution: 'temurin'

      - name: Navigate to function project directory
        run: cd ${{ env.FUNCTION_PROJECT_PATH }}

      - name: Build with Maven
        run: |
          cd ./AzureJavaFunctionDeploy
          mvn clean package

      - name: Zip the Azure Java Function Deploy folder
        run: |
          cd ${{ env.FUNCTION_PROJECT_PATH }}
          zip -r ../AzureFunctionJavaDeploy.zip ./*

      - name: Login to Azure
        uses: azure/login@v1
        with:
          creds: |
            {
              "clientId": "${{ secrets.AZURE_CLIENT_ID }}",
              "clientSecret": "${{ secrets.AZURE_CLIENT_SECRET }}",
              "tenantId": "${{ secrets.AZURE_TENANT_ID }}",
              "subscriptionId": "${{ secrets.AZURE_SUBSCRIPTION_ID }}"
            }

      - name: Deploy to Azure Function App
        run: |
          az functionapp deployment source config-zip \
            --resource-group "demofunctionapp-rg" \
            --name "${{ env.AZURE_FUNCTIONAPP_NAME }}" \
            --src "./AzureFunctionJavaDeploy.zip"
