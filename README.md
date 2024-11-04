# Projeto de Tradução com Azure Translator

## Configurações no Azure

1. Acesse o portal do Azure: [Azure Portal](https://portal.azure.com/).
2. Crie um novo recurso de Translator:
   - Clique em "Criar um recurso".
   - Pesquise por "Translator" e selecione "Translator".
   - Preencha as informações necessárias e clique em "Criar".

3. Obtenha a chave e a localização:
   - Após a criação do recurso, vá para a página do recurso.
   - Navegue até "Keys and Endpoint".
   - Copie a chave e a localização.

4. Crie variáveis de ambiente:
   - Abra o PowerShell.
   - Execute os seguintes comandos substituindo `{sua_chave}` e `{sua_regiao}` pelos valores copiados:

```pwsh
[System.Environment]::SetEnvironmentVariable('AZURE_SUBSCRIPTION_KEY', '{sua_chave}', [System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable('AZURE_REGION', '{sua_regiao}', [System.EnvironmentVariableTarget]::User)
```

![ezgif-6-49595dfe30](https://github.com/user-attachments/assets/7c4382a3-3d31-4fd5-a088-67b0a3485e37)


## Referências 
[Documentação do tradutor de IA do Azure](https://learn.microsoft.com/pt-br/azure/ai-services/translator/?WT.mc_id=Portal-Microsoft_Azure_ProjectOxford)
